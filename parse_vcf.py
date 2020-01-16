import sys
import argparse

##### parse arguments
parser = argparse.ArgumentParser(description="Parse vcf files by deleting metadata and keeping only selected columns.");
parser.add_argument('-i', '--input', required=True, help="The name of the input vcf file.");
parser.add_argument('-o', '--output', required=False, help="The name of the file to output to (will overwrite file if it already exists). If this argument is not specified, output will be to stdout.");
parser.add_argument('-c', '--columns', nargs='+', type=str, required=True, help="The columns that you wish to keep. Must be in order and ascending and space delimited. 1 indexed. Can also include hyphenated ranges (inclusive), such as 2-8 (all columns between 2 and 8)");

_args = parser.parse_args();
globals()['args'] = _args;
#####

def parseLine(line, outfile):

    line = line.split(); 

    curr_col_num = 1;
    curr_arg_pos = 0;
    max_col = len(col_args);

    for col in line:
        # if the column was specified by the user, print the column
        if curr_col_num == col_args[curr_arg_pos]:
            curr_arg_pos += 1; 
            if (curr_arg_pos == max_col):
                outfile.write(col);
                break;
            outfile.write(col + '\t');

        curr_col_num += 1;

    outfile.write('\n');


##### ___main___ #####

vcf_file_name = args.input;

#if vcf_file_name[-4:] != ".vcf":
#    print("Input file is not a .vcf file");
#    sys.exit();

if vcf_file_name == args.output:
    print("Input and output should not be the same file")
    sys.exit()

vcf_file = open(vcf_file_name);
if args.output != None:
    parsed_vcf_stream = open(args.output, "w");
else:
    parsed_vcf_stream = sys.stdout;

#Parse column arguments into a list of columns
cols = []
for col in args.columns:
    if "-" in col:
        col_range = col.split("-")
        cols.extend(range(int(col_range[0]), int(col_range[1]) + 1))
    else:
        cols.append(int(col))
globals()['col_args'] = cols

for line in vcf_file:
    if line[0] != '#':
        # Make sure the user did not specify too large of a column
        test_line = line.split();
        if len(test_line) < col_args[-1]:
            print("The columns you specified are greater than the actual number of columns in the file...");
            print("exiting...");
            sys.exit();

        # first line of real data
        parseLine(line, parsed_vcf_stream);
        break;
for line in vcf_file:
    parseLine(line, parsed_vcf_stream);

#########################
