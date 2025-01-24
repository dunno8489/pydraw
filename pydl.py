import xml.etree.ElementTree as xmltree
import os as sysapi
def chprojdir(changeto):
    sysapi.chdir(changeto)
def loadproj(filename):
    proj=xmltree.parse(filename)
    rt=proj.getroot()
chprojdir("examples")
loadproj("square.pdp")