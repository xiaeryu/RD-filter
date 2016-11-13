RD-filter
===

#### Step 1. Generate depth files
This should be conducted for each sample. Just use the '.sort.bam' file generated while calling variant (where H37Rv is used as the reference genome).

```shell
samtools depth $prefix.sort.bam > $prefix.depth
```
#### Step 2. Format t-test input
[Python script formatDepth.py](https://github.com/xiaeryu/RD-filter/blob/master/formatDepth.py)  
[Example ist of prefixes to include](https://github.com/xiaeryu/RD-filter/blob/master/example_list_of_prefix)  
[Example summary of sequencing read depth](https://github.com/xiaeryu/RD-filter/blob/master/example_list_of_depth)  

This should be conducted each for the two groups you want to compare, generating two outputs: output_name_for_ttest.1 and output_name_for_ttest.2

```shell
python formatDepth.py example_list_of_prefix directory_to_depth_files example_list_of_depth output_name_for_ttest
```
#### Step 3. Conduct t-test position-by-position
[R script t-test.r](https://github.com/xiaeryu/RD-filter/blob/master/t-test.r)  

```shell
Rscript t-test.r output_name_for_ttest.1 output_name_for_ttest.2 final_output
```
