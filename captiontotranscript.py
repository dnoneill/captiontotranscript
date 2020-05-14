import os
import webvtt

path = input('Filepath where your files are located: ')
files = [os.path.join(path, name) for path, subdirs, files in os.walk(path) for name in files]
captionfiles = ['.srt', '.webvtt', '.vtt']
for f in files:
    extension = os.path.splitext(f)[-1]
    if extension.lower() in captionfiles:
        try:
            if extension == '.srt':
                caption = webvtt.from_srt(f)
            else:
                caption = webvtt.read(f)
            txtcontent = []
            for cap in caption:
                txtcontent.append(cap.text)
                outputtxt = os.path.basename(f).replace(extension, '.txt')
                with open(outputtxt, 'w') as outputfile:
                    outputfile.write('\n'.join(txtcontent))
        except Exception as e:
            print("{} for {}".format(e, f))
