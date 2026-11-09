# Rebuilds the site from the finished movie: python3 -I build.py   (needs ../intro/cues.json and gates.json from scene.py gates)
import json, subprocess
EN = '../intro/Braces intro v1.mp4'
def ff(*a): subprocess.run(['ffmpeg', '-v', 'error', '-y', *a], check=True)
ff('-i', EN, '-c', 'copy', '-bsf:v', 'h264_metadata=colour_primaries=1:transfer_characteristics=1:matrix_coefficients=6', '-movflags', '+faststart', 'media/en.mp4')   # say which colours these are, so browsers show the page's yellow
c = {'en': [v[0] for v in json.load(open('../intro/cues.json'))['segs'].values()]}
g = {'en': json.load(open('../intro/gates.json'))}
open('index.html', 'w').write(open('template.html').read().replace('/*CUES*/', json.dumps(c)).replace('/*GATES*/', json.dumps(g)))
t = 160.0                                       # Yeti's big braces-off smile, with the sparkles
ff('-ss', str(t), '-i', EN, '-frames:v', '1', '-q:v', '3', 'media/poster.jpg')
ff('-ss', '78', '-i', EN, '-frames:v', '1', '-vf', 'crop=1949:1024:163:0,scale=1200:630', 'preview.png')       # the colourful bands on the teeth
