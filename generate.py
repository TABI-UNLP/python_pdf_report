from xhtml2pdf import pisa
from jinja2 import Template
import os
import sys
from pathlib import Path

data = {
    'equipo' : 'River Plate', 
    'dt' : 'Marcelo Gallardo'
    }

base_dir = os.path.dirname(os.path.abspath(__file__))

def convertHtmlToPdf(file, data):
    output_file = str(Path(file).with_suffix('.pdf'))
    resultFile = open(output_file, "w+b")
    template = Template(open(file).read())
    html  = template.render(data)
    pisaStatus = pisa.CreatePDF(
            html,
            dest=resultFile)
    resultFile.close()
    return pisaStatus.err

if __name__=="__main__":
    pisa.showLogging()
    file = os.path.join(base_dir, sys.argv[1])
    convertHtmlToPdf(file, data)
    #print(sys.argv[1])
