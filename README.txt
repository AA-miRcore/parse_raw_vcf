#################

parse_vcf documentation

author:	Jae Chan Hwang (hwangjc@umich.edu)
updater: Nolan Kuza (nkuza8@gmail.com)
date:	10-03-2018
update_date:	11-17-18

#################

Parse vcf files by deleting metadata and keeping only selected columns.

usage: parse_vcf.py [-h] -i INPUT [-o OUTPUT] -c COLUMNS [COLUMNS ...]

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        The name of the file to output to (will overwrite file
                        if it already exists). If this argument is not
                        specified, output will be to stdout.  

required arguments:
  -i INPUT, --input INPUT
                        The name of the input vcf file.
  -c COLUMNS [COLUMNS ...], --columns COLUMNS [COLUMNS ...]
                        The columns that you wish to keep. Must be in order
                        and ascending and space delimited. 1 indexed.
						Can also include hyphenated ranges (inclusive), such as 2-8 (all columns between 2 and 8)
 

example:

	There is a vcf file named patient.vcf
	We want to keep columns 1 2 3 4 7 9
	And write to patient.new.vcf

	Then run with:
		
		python parsed_vcf.py -i patient.vcf -o patient.new.vcf -c 1-4 7 9

	The program will output patient.new.vcf

other:
	If you specify a column number that is too high, for example,
	you specify column 30 and there are only 12 columns in the file,
	the program will exit with an error message.

	Make sure the file has extension .vcf
