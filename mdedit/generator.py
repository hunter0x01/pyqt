'''
Created on Mar 10, 2015

@author: Sylvain Garcia <garcia.6l20@gmail.com>
'''

from markdown import *
from markdown.extensions.toc import TocExtension
from markdown.extensions.fenced_code import FencedCodeExtension
from markdown.extensions.tables import TableExtension
from markdown.extensions.admonition import AdmonitionExtension
from markdown.extensions.codehilite import CodeHiliteExtension
from weasyprint import HTML, CSS
import os
import re
import tempfile

class Generator(object):
    '''
    classdocs
    '''

    @staticmethod
    def generateHTML(md_filename=None,source=None,css=None):
        if md_filename is None:
            if source is None:
                raise ValueError('You must supply md_filename or source')
            html_filename = tempfile.mktemp('html', 'md-edit')
        else:
            with open(md_filename,'r') as f:
                source = f.read()
            html_filename = os.path.splitext(md_filename)[0] + '.html'
        
        extras=['fenced-code-blocks','toc','footnotes','wiki-tables','code-friendly']
        extensions=[
            TocExtension(baselevel=3),
            FencedCodeExtension(),
            TableExtension(),
            AdmonitionExtension(),
            CodeHiliteExtension()
        ]
        
        
        html = Markdown(extras=extras,extensions=extensions).convert(source)
        
        # custom postprocess
        
        # strike
        strike_pathern = re.compile(r'~{2}(.*?)~{2}')
        html = re.sub(strike_pathern, r'<del>\1</del>', html)
        
        # quoted
        quoted_pathern = re.compile(r'\:\"(.*?)\"\:')
        html = re.sub(quoted_pathern, r'&ldquo;\1&rdquo;', html)
        
        with open(html_filename,'w') as f:            
            f.write(html)
        
        if not css is None:
            html = '<style>' + css + '</style>' + html
        
        return html
        
    @staticmethod
    def generatePDF(md_filename):
        html_filename = os.path.splitext(md_filename)[0] + '.html'
        pdf_filename = os.path.splitext(md_filename)[0] + '.pdf'
        css_filename = 'css/default.css'
        
        Generator.generateHTML(md_filename)
            
        HTML(html_filename).write_pdf(
            pdf_filename,
            stylesheets=[
                CSS(filename=css_filename)
            ]
        )
