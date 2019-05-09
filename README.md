# tfdread

Python package to read data from TFD files used in geophysical logging.

I'm working from the incredibly helpful paper by 
[Liang and Zhang (2015)](https://www.researchgate.net/publication/301431667_Decoding_and_Conversion_of_TFD_Logging_Data_Format_Based_on_Java).

## Install 

```posh
> pip install git+https://github.com/kinverarity1/tfdread#egg=tfdread
```

## Usage

The API ***will*** change as development proceeds.

For now, the function ``tfdread.read_file(file_obj)`` returns a dictionary.

```python
>>> import tfdread
>>> with open('blahblah.tfd', 'rb') as f:
...     j = tfdread.read_file(f)
```

When using the included command line script, this will be dumped to JSON:

```posh
> tfdread blahblah.tfd
{
  "IndexA": {
    "i1": 10476
  },
  "IndexADate": {
    "date": "b'\\xe3\\x07\\x04\\x00\\x04\\x00\\x04\\x00\\x0b\\x00\\x07\\x00'"
  },
  "IndexB": {
    "i2": 12104
  },
  "IndexC": {
    "l": 277
  },
  "InfoA": {
    "contents": "C:\\Logger\\Tools\\TOOLSTACK.descrU(\u0000\u0000; BEGINNING OF
MERGED SUBS SECTIONS //////////////////////////////////\r\n\r\n[Description]\r\n
ToolName = GO7-40-DEV-FTC\r\nDriverName = TOOLSTACK\r\nFamilyName = \r\nSub1 = T
ool Top,GO7-40,,\r\nSub2 = Misc,DEV,134607,MULTICH\r\nSub3 = Fluid,FTC,6023,MULT
ICH\r\n\r\n[Default]\r\nTimeSamplingRate=500\r\nDepthSamplingRate=0.05\r\n\r\n[M
ultiCh]\r\nNbCh = 25\r\nToolLength = 1.559\r\n\r\n[ToolId]]\r\nDEV = 21\r\nFTC =
 25\r\n\r\n[DEV.ModuleId]\r\nSYSTEMSTATUS = 1\r\nAPS544 = 3\r\n\r\n[FTC.ModuleId
]\r\nSYSTEMSTATUS = 1\r\nFTC = 5\r\nTEMPERATURE = 2\r\n\r\n; GO7-40 channels ---
---------------------\r\n\r\n; DEV channels ------------------------\r\n\r\n[Ch1
]\r\nName=Time\r\nProducer=Tool.DEV.SYSTEMSTATUS\r\nChShift=1.137\r\nUnit=sec\r\
nOffset=0\r\nDataType=dword\r\nCalA=0.001\r\nCalB=0\r\nNumberFormat=%8.3f\r\nDis
playEnable=no\r\nReference1=1\r\nReference2=0\r\nCalDate=25/01/18 13:34\r\n\r\n[
Ch2]\r\nName=Temperature\r\nProducer=Tool.DEV.SYSTEMSTATUS\r\nChShift=1.137\r\nU
nit='C\r\nOffset=4\r\nDataType=word\r\nCalA=0.217226\r\nCalB=-61.11\r\nNumberFor
mat=%5.1f\r\nDisplayEnable=no\r\nDisplayedName=Temp\r\nLow=0\r\nHigh=70\r\nNbDec
ade=1\r\nMode=Linear\r\nReverseScale=no\r\nGridEnable=yes\r\nGrid=10\r\nLeft=60\
r\nRight=80\r\nPenStyle=solid\r\nPenWidth=2\r\nPenColor=0\r\n\r\n[Ch3]\r\nName=R
oll\r\nProducer=Tool.DEV.APS544\r\nChShift=1.137\r\nUnit=deg\r\nOffset=0\r\nData
Type=short\r\nCalA=0.1\r\nCalB=0\r\nNumberFormat=%7.1f\r\nDisplayEnable=no\r\n\r
\n[Ch4]\r\nName=MRoll\r\nProducer=Tool.DEV.APS544\r\nChShift=1.137\r\nUnit=deg\r
\nOffset=2\r\nDataType=short\r\nCalA=0.1\r\nCalB=0\r\nNumberFormat=%7.1f\r\nDisp
layEnable=no\r\n\r\n[Ch5]\r\nName=Tilt\r\nProducer=Tool.DEV.APS544\r\nChShift=1.
137\r\nUnit=deg\r\nOffset=4\r\nDataType=short\r\nCalA=0.1\r\nCalB=0\r\nNumberFor
mat=%7.1f\r\nDisplayEnable=yes\r\nLow=0\r\nHigh=15\r\nNbDecade=1\r\nMode=Linear\
r\nReverseScale=no\r\nGridEnable=no\r\nGrid=2.5\r\nLeft=40\r\nRight=60\r\nPenSty
le=solid\r\nPenWidth=2\r\nPenColor=ff0000\r\n\r\n[Ch6]\r\nName=MagField\r\nProdu
cer=Tool.DEV.APS544\r\nChShift=1.137\r\nUnit=uT\r\nOffset=6\r\nDataType=short\r\
nCalA=0.01\r\nCalB=0\r\nNumberFormat=%7.2f\r\nDisplayEnable=no\r\n\r\n[Ch7]\r\nN
ame=Azimut\r\nProducer=Tool.DEV.APS544\r\nChShift=1.137\r\nUnit=deg\r\nOffset=8\
r\nDataType=short\r\nCalA=0.1\r\nCalB=0\r\nNumberFormat=%7.1f\r\nDisplayEnable=y
es\r\nLow=0\r\nHigh=360\r\nNbDecade=1\r\nMode=Linear\r\nReverseScale=no\r\nGridE
nable=yes\r\nGrid=45\r\nLeft=40\r\nRight=60\r\nPenStyle=solid\r\nPenWidth=2\r\nP
enColor=ff\r\n\r\n[Ch8]\r\nName=Grav\r\nProducer=Tool.DEV.APS544\r\nChShift=1.13
7\r\nUnit=g\r\nOffset=10\r\nDataType=short\r\nCalA=0.0001\r\nCalB=0\r\nNumberFor
mat=%7.4f\r\nDisplayEnable=no\r\n\r\n[Ch9]\r\nName=TDev\r\nProducer=Tool.DEV.APS
544\r\nChShift=1.137\r\nUnit='C\r\nOffset=12\r\nDataType=short\r\nCalA=0.01\r\nC
alB=0\r\nNumberFormat=%7.1f\r\nDisplayEnable=no\r\nLow=0\r\nHigh=70\r\nNbDecade=
1\r\nMode=Linear\r\nReverseScale=no\r\nGridEnable=no\r\nGrid=0\r\nLeft=60\r\nRig
ht=80\r\nPenStyle=solid\r\nPenWidth=3\r\nPenColor=ff0000\r\n\r\n[Ch10]\r\nName=V
oltage\r\nProducer=Tool.DEV.APS544\r\nChShift=1.137\r\nUnit=V\r\nOffset=14\r\nDa
taType=short\r\nCalA=0.0001\r\nCalB=0\r\nNumberFormat=%7.4f\r\nDisplayEnable=no\
r\n\r\n[Ch11]\r\nName=MX\r\nProducer=Tool.DEV.APS544\r\nChShift=0.965\r\nUnit=uT
\r\nOffset=16\r\nDataType=short\r\nCalA=0.01\r\nCalB=0\r\nNumberFormat=%7.2f\r\n
DisplayEnable=no\r\nDisplayedName=MX\r\nLow=0\r\nHigh=1\r\nNbDecade=1\r\nMode=Li
near\r\nReverseScale=no\r\nGridEnable=no\r\nGrid=0\r\nLeft=80\r\nRight=100\r\nPe
nStyle=solid\r\nPenWidth=1\r\nPenColor=ff\r\n\r\n[Ch12]\r\nName=AX\r\nProducer=T
ool.DEV.APS544\r\nChShift=0.965\r\nUnit=g\r\nOffset=18\r\nDataType=short\r\nCalA
=0.0001\r\nCalB=0\r\nNumberFormat=%7.4f\r\nDisplayEnable=no\r\nDisplayedName=AX\
r\nLow=0\r\nHigh=1\r\nNbDecade=1\r\nMode=Linear\r\nReverseScale=no\r\nGridEnable
=no\r\nGrid=0\r\nLeft=80\r\nRight=100\r\nPenStyle=solid\r\nPenWidth=1\r\nPenColo
r=ff0000\r\n\r\n[Ch13]\r\nName=MY\r\nProducer=Tool.DEV.APS544\r\nChShift=0.965\r
\nUnit=uT\r\nOffset=20\r\nDataType=short\r\nCalA=0.01\r\nCalB=0\r\nNumberFormat=
%7.2f\r\nDisplayEnable=no\r\nDisplayedName=MY\r\nLow=0\r\nHigh=1\r\nNbDecade=1\r
\nMode=Linear\r\nReverseScale=no\r\nGridEnable=no\r\nGrid=0\r\nLeft=80\r\nRight=
100\r\nPenStyle=solid\r\nPenWidth=1\r\nPenColor=80ff\r\n\r\n[Ch14]\r\nName=AY\r\
nProducer=Tool.DEV.APS544\r\nChShift=0.965\r\nUnit=g\r\nOffset=22\r\nDataType=sh
ort\r\nCalA=0.0001\r\nCalB=0\r\nNumberFormat=%7.4f\r\nDisplayEnable=no\r\nDispla
yedName=AY\r\nLow=0\r\nHigh=1\r\nNbDecade=1\r\nMode=Linear\r\nReverseScale=no\r\
nGridEnable=no\r\nGrid=0\r\nLeft=80\r\nRight=100\r\nPenStyle=solid\r\nPenWidth=1
\r\nPenColor=ff8080\r\n\r\n[Ch15]\r\nName=MZ\r\nProducer=Tool.DEV.APS544\r\nChSh
ift=0.965\r\nUnit=uT\r\nOffset=24\r\nDataType=short\r\nCalA=0.01\r\nCalB=0\r\nNu
mberFormat=%7.2f\r\nDisplayEnable=no\r\nDisplayedName=MZ\r\nLow=0\r\nHigh=1\r\nN
bDecade=1\r\nMode=Linear\r\nReverseScale=no\r\nGridEnable=no\r\nGrid=0\r\nLeft=8
0\r\nRight=100\r\nPenStyle=solid\r\nPenWidth=1\r\nPenColor=ff00ff\r\n\r\n[Ch16]\
r\nName=AZ\r\nProducer=Tool.DEV.APS544\r\nChShift=0.965\r\nUnit=g\r\nOffset=26\r
\nDataType=short\r\nCalA=0.0001\r\nCalB=0\r\nNumberFormat=%7.4f\r\nDisplayEnable
=no\r\nDisplayedName=AZ\r\nLow=0\r\nHigh=1\r\nNbDecade=1\r\nMode=Linear\r\nRever
seScale=no\r\nGridEnable=no\r\nGrid=0\r\nLeft=80\r\nRight=100\r\nPenStyle=solid\
r\nPenWidth=1\r\nPenColor=ffff00\r\n\r\n; FTC channels ------------------------\
r\n\r\n[Ch17]\r\nName=Time\r\nProducer=Tool.FTC.SYSTEMSTATUS\r\nUnit=sec\r\nChSh
ift=0\r\nDataType=DWord\r\nOffset=0\r\nCalA=0.001\r\nCalB=0\r\nCalibrationEnable
=no\r\nNumberFormat=%8.3f\r\nDisplayEnable=no\r\n\r\n[Ch18]\r\nName=TCPU\r\nProd
ucer=Tool.FTC.SYSTEMSTATUS\r\nUnit='C\r\nChShift=0.063\r\nDataType=Word\r\nOffse
t=4\r\nCalA=0.217226\r\nCalB=-61.11\r\nCalibrationEnable=no\r\nNumberFormat=%5.1
f\r\nDisplayEnable=no\r\n\r\n[Ch19]\r\nName=Vinj\r\nProducer=Tool.FTC.FTC\r\nUni
t=V\r\nChShift=0.0642\r\nDataType=long\r\nOffset=0\r\nCalA=1.16767e-006\r\nCalB=
-0.0508554\r\nCalibrationEnable=no\r\nNumberFormat=%8.3f\r\nDisplayEnable=no\r\n
DisplayedName=Vinj\r\nLow=0\r\nHigh=15\r\nNbDecade=1\r\nMode=Linear\r\nReverseSc
ale=no\r\nGridEnable=no\r\nGrid=0\r\nLeft=0\r\nRight=30\r\nPenStyle=solid\r\nPen
Width=1\r\nPenColor=ff\r\nQCLow=0\r\nQCHigh=0\r\nQCLowRangeColor=2\r\nQCMedRange
Color=1\r\nQCHighRangeColor=2\r\nQCLowRangeText=Invalid\r\nQCMedRangeText=Valid\
r\nQCHighRangeText=Invalid\r\nQCLowRangeBeep=no\r\nQCMedRangeBeep=no\r\nQCHighRa
ngeBeep=no\r\nFilter=1\r\nReference1=9.204\r\nReference2=0\r\nCalDate=30/06/14 1
5:39\r\n\r\n[Ch20]\r\nName=Iinj\r\nProducer=Tool.FTC.FTC\r\nUnit=mA\r\nChShift=0
.0642\r\nDataType=long\r\nOffset=4\r\nCalA=7.56269e-006\r\nCalB=-0.00415192\r\nC
alibrationEnable=no\r\nNumberFormat=%8.1f\r\nDisplayEnable=no\r\nDisplayedName=I
inj\r\nLow=0\r\nHigh=100\r\nNbDecade=1\r\nMode=Linear\r\nReverseScale=no\r\nGrid
Enable=yes\r\nGrid=10\r\nLeft=0\r\nRight=30\r\nPenStyle=solid\r\nPenWidth=1\r\nP
enColor=80ff\r\nQCLow=0\r\nQCHigh=0\r\nQCLowRangeColor=2\r\nQCMedRangeColor=1\r\
nQCHighRangeColor=2\r\nQCLowRangeText=Invalid\r\nQCMedRangeText=Valid\r\nQCHighR
angeText=Invalid\r\nQCLowRangeBeep=no\r\nQCMedRangeBeep=no\r\nQCHighRangeBeep=no
\r\nFilter=1\r\nReference1=89.81\r\nReference2=0\r\nCalDate=30/06/14 15:38\r\n\r
\n[Ch21]\r\nName=DV1\r\nProducer=Tool.FTC.FTC\r\nUnit=V\r\nChShift=0.0642\r\nDat
aType=long\r\nOffset=16\r\nCalA=5.43396e-007\r\nCalB=-0.00026083\r\nCalibrationE
nable=no\r\nNumberFormat=%8.3f\r\nDisplayEnable=no\r\nDisplayedName=DV1\r\nLow=0
\r\nHigh=1\r\nNbDecade=1\r\nMode=Linear\r\nReverseScale=no\r\nGridEnable=no\r\nG
rid=0\r\nLeft=0\r\nRight=30\r\nPenStyle=solid\r\nPenWidth=1\r\nPenColor=8000\r\n
QCLow=0\r\nQCHigh=0\r\nQCLowRangeColor=2\r\nQCMedRangeColor=1\r\nQCHighRangeColo
r=2\r\nQCLowRangeText=Invalid\r\nQCMedRangeText=Valid\r\nQCHighRangeText=Invalid
\r\nQCLowRangeBeep=no\r\nQCMedRangeBeep=no\r\nQCHighRangeBeep=no\r\nFilter=1\r\n
Reference1=3.058\r\nReference2=0\r\nCalDate=30/06/14 15:41\r\n\r\n[Ch22]\r\nName
=DV2\r\nProducer=Tool.FTC.FTC\r\nUnit=V\r\nChShift=0.0642\r\nDataType=long\r\nOf
fset=8\r\nCalA=5.51344e-007\r\nCalB=-0.000272364\r\nCalibrationEnable=no\r\nNumb
erFormat=%8.3f\r\nDisplayEnable=no\r\nDisplayedName=DV2\r\nLow=0\r\nHigh=1\r\nNb
Decade=1\r\nMode=Linear\r\nReverseScale=no\r\nGridEnable=no\r\nGrid=0\r\nLeft=0\
r\nRight=30\r\nPenStyle=solid\r\nPenWidth=1\r\nPenColor=ff0000\r\nQCLow=0\r\nQCH
igh=0\r\nQCLowRangeColor=2\r\nQCMedRangeColor=1\r\nQCHighRangeColor=2\r\nQCLowRa
ngeText=Invalid\r\nQCMedRangeText=Valid\r\nQCHighRangeText=Invalid\r\nQCLowRange
Beep=no\r\nQCMedRangeBeep=no\r\nQCHighRangeBeep=no\r\nFilter=1\r\nReference1=3.0
82\r\nReference2=0\r\nCalDate=30/06/14 15:42\r\n\r\n[Ch23]\r\nName=Temp\r\nProdu
cer=Tool.FTC.FTC\r\nUnit='C\r\nChShift=0\r\nChShift=0\r\nDataType=long\r\nOffset
=12\r\nCalA=0.00392394\r\nCalB=-277.75\r\nReference1=7.2\r\nReference2=78.1\r\nC
alDate=01/07/14 09:36\r\nCalibrationEnable=no\r\nNumberFormat=%8.2f\r\nDisplayEn
able=yes\r\nDisplayedName=Temp\r\nLow=10\r\nHigh=20\r\nNbDecade=1\r\nMode=Linear
\r\nReverseScale=no\r\nGridEnable=yes\r\nGrid=1\r\nLeft=35\r\nRight=67.5\r\nPenS
tyle=solid\r\nPenWidth=2\r\nPenColor=ff\r\nQCLow=0\r\nQCHigh=0\r\nQCLowRangeColo
r=2\r\nQCMedRangeColor=1\r\nQCHighRangeColor=2\r\nQCLowRangeText=Invalid\r\nQCMe
dRangeText=Valid\r\nQCHighRangeText=Invalid\r\nQCLowRangeBeep=no\r\nQCMedRangeBe
ep=no\r\nQCHighRangeBeep=no\r\nFilter=1\r\n\r\n[Ch24]\r\nName=Cond\r\nProducer=M
ChProc\r\nFormula=(148.526*{ch20})/({ch21}+{ch22})\r\nUnit=uS/cm\r\nCalibrationE
nable=yes\r\nChShift=0.0642\r\nCalA=1.15821\r\nCalB=4.59802\r\nReference1=5055\r
\nReference2=112\r\nCalDate=01/07/14 08:40\r\nNumberFormat=%8.1f\r\nDisplayEnabl
e=yes\r\nDisplayedName=Cond\r\nLow=0\r\nHigh=10000\r\nNbDecade=1\r\nMode=Linear\
r\nReverseScale=no\r\nGridEnable=no\r\nGrid=0\r\nLeft=0\r\nRight=30\r\nPenStyle=
solid\r\nPenWidth=1\r\nPenColor=ff8000\r\nQCLow=0\r\nQCHigh=0\r\nQCLowRangeColor
=2\r\nQCMedRangeColor=1\r\nQCHighRangeColor=2\r\nQCLowRangeText=Invalid\r\nQCMed
RangeText=Valid\r\nQCHighRangeText=Invalid\r\nQCLowRangeBeep=no\r\nQCMedRangeBee
p=no\r\nQCHighRangeBeep=no\r\nFilter=1\r\n\r\n[Ch25]\r\nName=Cond25C\r\nProducer
=MChProc\r\nFormula=46.5*{ch24}/({ch23}+21.5)\r\nUnit=uS/cm\r\nChShift=0.0642\r\
nCalA=1\r\nCalB=0\r\nCalibrationEnable=no\r\nNumberFormat=%8.1f\r\nDisplayEnable
=no\r\nDisplayedName=Cond25C\r\nLow=0\r\nHigh=10000\r\nNbDecade=3\r\nMode=Logary
thmic\r\nReverseScale=no\r\nGridEnable=yes\r\nGrid=0\r\nLeft=67.5\r\nRight=100\r
\nPenStyle=solid\r\nPenWidth=2\r\nPenColor=ff8000\r\nQCLow=0\r\nQCHigh=0\r\nQCLo
wRangeColor=2\r\nQCMedRangeColor=1\r\nQCHighRangeColor=2\r\nQCLowRangeText=Inval
id\r\nQCMedRangeText=Valid\r\nQCHighRangeText=Invalid\r\nQCLowRangeBeep=no\r\nQC
MedRangeBeep=no\r\nQCHighRangeBeep=no\r\nFilter=1\r\n\r\n; GO7-40 channels calib
rations ------------------------\r\n\r\n; DEV channels calibrations ------------
------------\r\n\r\n; FTC channels calibrations ------------------------\r\n\r\n
[Process]\r\nProcess1 = Processor,Start,mch\\MChProc.exe\r\nProcess2 = Browser,S
tart,MCh\\MChNum.exe\r\nProcess3 = Browser,Start,MCh\\MChCurve.exe\r\n\r\n[MChPr
oc]\r\nMinimized=no\r\nXOffset=797\r\nYOffset=363\r\nXSize=302\r\nYSize=135\r\n\
r\n[MChNum]\r\nNumDisplay1=Ch5\r\nNbNumDisplay=6\r\nNumDisplay2=Ch7\r\nNumDispla
y3=Ch8\r\nNumDisplay4=Ch6\r\nNumDisplay5=Ch23\r\nNumDisplay6=Ch24\r\nXOffset=584
\r\nYOffset=173\r\nXSize=304\r\nYSize=356\r\nMinimized=no\r\n\r\n[MChCurve]\r\nD
epthScale=100\r\nGridSpacing=0.5\r\nXOffset=584\r\nForceTimeMode=no\r\nYSize=728
\r\nDepthColLeft=0.3\r\nXSize=776\r\nDepthSpacing=5\r\nDepthColRight=0.35\r\nMin
imized=no\r\nYOffset=0\r\nGrid=yes\r\n\r\n[WellCAD]\r\n\r\n; END OF MERGED SUBS
SECTIONS ////////////////////////////////////////\r\n\r\nTemplate1=\r\n"
  }
}
```

MIT license.