# flickr-caption-score

Some helpers for Flickr30k Datasets to calculate language metrics using [Microsoft COCO Caption Evaluation code](https://github.com/tylin/coco-caption). 

AFAIK, Since Flickr30k dataset images are not labeled as train/test/val, we can use Flickr8k test images to create a baseline. So we need both Flickr30k and Flickr8k Datasets to achieve our goals.

Here i used output of [NeuralTalk2](https://github.com/karpathy/neuraltalk2) to create result json. While running test of NeuralTalk2, you should enable the -dump_path option to get file names properly, instead of 1.jpg, 2.jpg so on.

[Create Baseline](flickr30k_create_baseline_json.py):
searches test files using Flickr8k test image names. And creates a baseline json file.

[Create Test](flickr30k_create_result_json.py):
creates result json using vis.json file 


