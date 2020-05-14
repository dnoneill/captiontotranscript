import os
import pycaption
from pycaption import CaptionConverter, SRTReader, WebVTTReader, SAMIWriter,DFXPWriter, transcript

path = input('Filepath where your files are located: ')
files = [os.path.join(path, name) for path, subdirs, files in os.walk(path) for name in files]
captionfiles = ['.srt', '.webvtt', '.vtt']
for f in files:
    extension = os.path.splitext(f)[-1]
    if extension.lower() in captionfiles:
        converter = CaptionConverter()
        if extension == '.srt':
            reader = SRTReader()
        else:
            reader = WebVTTReader()
        try:
            content = converter.read(open(f).read(), reader)
            txtcontent = converter.write(transcript.TranscriptWriter())
            outputtxt = os.path.basename(f).replace(extension, '.txt')
            with open(outputtxt, 'w') as outputfile:
                outputfile.write(txtcontent)
        except Exception as e:
            print("{} for {}".format(e, f))
