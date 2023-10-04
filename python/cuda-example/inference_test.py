import torch
import pandas as pd
from torchvision import models, transforms
from PIL import Image

IMG_PATH = './images/peacock.jpg'
IMG_CLASSES = 'https://raw.githubusercontent.com/pytorch/hub/master/imagenet_classes.txt'

if __name__ == '__main__':

  model = models.resnet50(weights=models.ResNet50_Weights.DEFAULT)

  img = Image.open(IMG_PATH)

  transform = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize((0.485, 0.456, 0.406), (0.229, 0.224, 0.225))
  ])

  img_batch = torch.unsqueeze(transform(img), 0)

  model.eval()

  with torch.no_grad():  # this is not important for inference only for training
    outputs = model(img_batch)

    probabilities = torch.nn.functional.softmax(outputs[0], dim=0)

    categories = pd.read_csv(IMG_CLASSES, header=None)

    top_more_probables = 5

    more_probables, class_number = torch.topk(
      probabilities, top_more_probables)

    for i in range(top_more_probables):
      probability = more_probables[i].item()
      class_name = categories[0][int(class_number[i])]
      print(f'{class_name} - {probability:.2%}')
