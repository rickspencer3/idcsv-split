# idcsv-split
Tool for splitting large InfluxDB Flux CSV files into smaller files to aid ingestion.

Usage: 
```
$ idcsv-split filename
```

The resulting files will be named part*n*.csv, where "n" is a number up to the number of files created. Currently puts 100 tables in each file. 
