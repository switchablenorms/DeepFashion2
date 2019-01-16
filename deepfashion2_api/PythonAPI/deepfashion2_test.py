from pycocotools.coco import COCO
from pycocotools.cocoeval import COCOeval
import pylab
pylab.rcParams['figure.figsize'] = (10.0, 8.0)


#initialize ground truth api
cocoGt=COCO(annFile)


#initialize detections api
cocoDt=cocoGt.loadRes(resFile)


imgIds=sorted(cocoGt.getImgIds())

# evaluating clothes detection
cocoEval = COCOeval(cocoGt,cocoDt,'bbox')
cocoEval.params.imgIds  = imgIds
cocoEval.evaluate()
cocoEval.accumulate()
cocoEval.summarize()

# evaluating landmark and pose Estimation
cocoEval = COCOeval(cocoGt,cocoDt,'keypoints')
cocoEval.params.imgIds  = imgIds
cocoEval.evaluate()
cocoEval.accumulate()
cocoEval.summarize()

# evaluating clothes segmentation
cocoEval = COCOeval(cocoGt,cocoDt,'segm')
cocoEval.params.imgIds  = imgIds
cocoEval.evaluate()
cocoEval.accumulate()
cocoEval.summarize()