#!/bin/bash  

file1=$1  
file2=$2  

# Check if both files were provided  
if [ -z "$file1" ] || [ -z "$file2" ]; then  
    echo "Usage: $0 <file1> <file2>"  
    exit 1  
fi  

# Check if files exist  
if [[ ! -f $file1 || ! -f $file2 ]]; then  
    echo "One or both files do not exist."  
    exit 1  
fi  

# Compare files  
if cmp -s "$file1" "$file2"; then  
    echo "Files are identical."  
else  
    echo "Files are different."  
fi  