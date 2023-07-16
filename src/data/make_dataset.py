from pycocotools.coco import COCO
import os

dataDir = '/Users/farazmoradi/Downloads/val2017'
dataType = 'val2017'  # or 'train2017' or whatever you have
annFile = '{}/annotations/panoptic_{}.json'.format(dataDir, dataType)

coco = COCO(annFile)