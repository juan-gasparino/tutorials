#include <Arduino.h>
#include <LiquidCrystal.h>

// Transmit rate in bps
#define TX_RATE 5

// Pin assignments
#define TX_DATA 3
#define TX_CLK 2

#define PARITY 10
#define LCD_RS 9
#define LCD_EN 8
#define LCD_D7 7
#define LCD_D6 6
#define LCD_D5 5
#define LCD_D4 4

LiquidCrystal lcd(LCD_RS, LCD_EN, LCD_D4, LCD_D5, LCD_D6, LCD_D7);

const char* message = "Hello, world!";

void setup() {

	pinMode(TX_DATA, OUTPUT);
	pinMode(TX_CLK, OUTPUT);
	pinMode(PARITY, INPUT);

	// Initialize the LCD screen

	lcd.begin(16, 2);
	lcd.setCursor(0, 0);
	lcd.print(message);

	for (int byte_idx = 0; byte_idx < strlen(message); byte_idx++) {

		char tx_byte = message[byte_idx];

		// Clear the second line of the display
		lcd.noCursor();
		lcd.setCursor(0, 1);
		lcd.print("XXXXXXXX");
		lcd.setCursor(byte_idx, 0);
		lcd.cursor();

		for (int bit_idx = 0; bit_idx < 8; bit_idx++) {

			bool tx_bit = tx_byte & (0x80 >> bit_idx);

			digitalWrite(TX_DATA, tx_bit);
			delay((1000 / TX_RATE) / 2);

			// Update the LCD
			lcd.noCursor();
			lcd.setCursor(bit_idx, 1);
			lcd.print(tx_bit ? "1" : "0");
			lcd.setCursor(byte_idx, 0);
			lcd.cursor();

			digitalWrite(TX_CLK, HIGH);
			delay((1000 / TX_RATE) / 2);
			digitalWrite(TX_CLK, LOW);

		}

	}

	digitalWrite(TX_DATA, digitalRead(PARITY));

	delay((1000 / TX_RATE) / 2);
	digitalWrite(TX_CLK, HIGH);
	delay((1000 / TX_RATE) / 2);
	digitalWrite(TX_CLK, LOW);

	digitalWrite(TX_DATA, LOW);

}

void loop() {
	// put your main code here, to run repeatedly:
}