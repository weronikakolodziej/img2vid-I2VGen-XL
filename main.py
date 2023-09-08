from modelscope.pipelines import pipeline
from modelscope.outputs import OutputKeys

!pip install -r /content/sample_data/requirements.txt

pipe = pipeline(task='image-to-video', model='damo/Image-to-Video', model_revision='v1.1.0')

# IMG_PATH: your image path (url or local file)
output_video_path = pipe(IMG_PATH, output_video='./output.mp4')[OutputKeys.OUTPUT_VIDEO]
print(output_video_path)
