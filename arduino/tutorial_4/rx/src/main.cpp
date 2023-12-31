#include <Arduino.h>
#include <LiquidCrystal.h>

// Transmit rate in bps
#define RX_RATE 5

// Pin assignments
#define RX_DATA 3
#define RX_CLK 2

#define LCD_RS 9
#define LCD_EN 8
#define LCD_D7 7
#define LCD_D6 6
#define LCD_D5 5
#define LCD_D4 4

LiquidCrystal lcd(LCD_RS, LCD_EN, LCD_D4, LCD_D5, LCD_D6, LCD_D7);

char message[16];
volatile byte rx_byte = 0;
volatile int bit_position = 0;
volatile bool updateLCDSCreen = true;

void onClockPulse()
{

	bool rx_bit = digitalRead(RX_DATA);

	if (bit_position == 8)
	{
		rx_byte = 0;
		bit_position = 0;
	}

	if (rx_bit)
	{
		rx_byte |= (0x80 >> bit_position);
	}

	bit_position += 1;

	if (bit_position == 8)
	{
		strncat(message, (const char *)&rx_byte, 1);
	}

	updateLCDSCreen = true;
}

void setup()
{
	pinMode(RX_DATA, INPUT);
	strcpy(message, "");
	lcd.begin(16, 2);
	attachInterrupt(digitalPinToInterrupt(RX_CLK), onClockPulse, RISING);
}

void loop()
{

	if (updateLCDSCreen)
	{

		updateLCDSCreen = false;

		lcd.noCursor();
		lcd.setCursor(0, 0);
		lcd.print(message);
		lcd.setCursor(0, 1);

		for (int i = 0; i < 8; i += 1)
		{
			if (i < bit_position)
			{
				lcd.print(rx_byte & (0x80 >> i) ? "1" : "0");
			}
			else
			{
				lcd.print("  ");
			}
		}

		lcd.setCursor(strlen(message), 0);
		lcd.cursor();
	}
}