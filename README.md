Introduction

GlycoSLASH is software developed based on msSLASH (standing for mass spectral Searching using LocAlity Sensitive Hashing) was developed by Sujun Li and Haixu Tang, specifically for glycopeptides identification based on the pre-constructed glycopeptides library.

Prerequisites

msSLASH

Installation

1. please acquire msSLASH at https://github.com/COL-IU/msSLASH
2. install msSLASH per the requirements on the github
3. Change the msSLASH location at GlycoSLASH

Usage

1. Create an folder contains all the mgf files for glycopeptides identification. For example:
   makedir Test
   cp test.mgf Test
   In our respository, we already place a test mgf in the Test folder and a test mgf in the folder as well. 
2. Create a list file for mgf list files. For example:
   Test/nash96_r2_90min_22feb.mgf 
   in the test file. 
   In our respository, we have a test.list file for you to test. 
3. Run:
   ./GlycoSLASH test.list
4. Check the results at the Test folder. You will find results ending with ".GlycoSLASH.tsv"
5. Summarize the results, Run:
   python GlycoSLASHParser.py Test
   The output will be :
   Filename        UniqueID        Total Spectra   Spectra ID number       Ratio of ID
   nash96_r2_90min_22feb.mgf.GlycoSLASH.tsv        222     3616    350     0.0967920353982

Questions

Please contact Sujun Li (sujli@indiana.edu)

Acknowledgement

The paper is partially supported by National Institutes of Health (Grant No: 1U01CA225753-01 and 1R01GM130091-01A1).
