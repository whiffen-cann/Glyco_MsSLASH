Introduction
---
GlycoSLASH is software developed based on msSLASH (standing for mass spectral Searching using LocAlity Sensitive Hashing) was developed by Sujun Li and Haixu Tang, specifically for glycopeptides identification based on the pre-constructed glycopeptides library.

Prerequisites

msSLASH

Installation
---
1. git clone git@github.com:whiffen-cann/Glyco_MsSLASH.git
2. cd  GlycoSLASH/msSLASH/
3. bash install.sh

Usage
---
1. Create an folder contains all the mgf files for glycopeptides identification. For example:
   
   ```linux command
   mkdir Test
   cp test.mgf Test
   ```
   
   In our respository, we already place a test mgf in the Test folder and a test mgf in the folder as well.
   
3. Create a list file for mgf list files, one mgf file per line. For example , content in file <test.list> in this repository as belove:

   Test/nash96_r2_90min_22feb.mgf
   
5. Run:
   '''GlycoSLASH test.list'''
   
6. Check the results at the Test folder. You will find results ending with ".GlycoSLASH.tsv"
   
8. Summarize the results, Run:
   '''GlycoSLASHParser.py Test'''

   The output will be :
   Filename        UniqueID        Total Spectra   Spectra ID number       Ratio of ID
   nash96_r2_90min_22feb.mgf.GlycoSLASH.tsv        222     3616    350     0.0967920353982

Questions
---
Please contact Sujun Li (sujli@indiana.edu ),Can Wang (whiffen_cann@qq.com)

Acknowledgement
---
The paper is partially supported by National Institutes of Health (Grant No: 1U01CA225753-01 and 1R01GM130091-01A1).
