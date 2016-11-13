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

```shell
python formatDepth.py example_list_of_prefix directory_to_depth_files example_list_of_depth output_name_for_ttest
```
