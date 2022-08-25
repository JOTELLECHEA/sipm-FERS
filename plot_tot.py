# Written By : Jonathan O. Tellechea
# Team       : Carlos Perez, Thomas Anderson, Chris Neu
# Research   : Script to create plots of Time Over Threshold (ToT) data taken from CAEN FERS.
from ROOT import TCanvas,TH1F
import ROOT
import numpy as np
import matplotlib.pyplot as plt
import sys


if len(sys.argv) > 1:
    fileName = sys.argv[1]
    print('Opening:',fileName,'\n')

else:
    # fileName = 'dataFiles/Run3_ToT_0_0.txt'
    print('No Arguments Passed.\nExiting script.')
    sys.exit()

run = fileName[13:-12] 
board = fileName[-7]
channel = fileName[-5]

f = open(fileName,'r')
data = f.readlines()
events = len(data)

c1 = ROOT.TCanvas('c1','Canvas 1',1000,1000)
c1.SetLeftMargin(0.15)
c1.SetRightMargin(0.15)

h1 = ROOT.TH1D('ToT','ToT;[LSB];Counts',512,0,512)

for i in range(events):
	if int(data[i]) == 0:continue
	h1.SetBinContent(i,int(data[i]))
c1.cd(1)
h1.SetTitle('Run#'+ run + '_channel#' + channel)
h1.Draw()

c1.SaveAs('plot.pdf')