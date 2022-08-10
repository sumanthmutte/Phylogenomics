#!/usr/bin/env python

'''
Python wrapper to format the InterProScan results TSV file into the list with required domains
'''

from collections import defaultdict
import csv

# Open Interproscan TSV results file
reader = csv.reader(open('file.tsv')) 

# Put the results into a dictionary
result = defaultdict(list)
for row in reader:
    if not row: # if the row is empty
        pass
    else:
        key = row[0]
        v = row[10]
        if key in result and v in result[key]:
            pass
        else:
            result[key].append(v)

#print result
print

# Lists of domains (and combinations) to search in the above dictionary results
# Change the domains as needed; here is an example with domains from Auxin Response Factors (ARFs).
arfdomains_all1 = ['IPR003340','IPR010525','IPR000270']
arfdomains_all2 = ['IPR003340','IPR010525','IPR003311']
arfdomains_b3arf = ['IPR003340','IPR010525']
arfdomains_arfpb1 = ['IPR010525','IPR000270']
arfdomains_arfauxiaa = ['IPR010525','IPR003311']
arfdomains_b3pb1 = ['IPR003340','IPR000270']
arfdomains_b3auxiaa = ['IPR003340','IPR003311']
arfdomains_arfap2 = ['IPR010525','IPR001471']
arfdomains_b3ap2 = ['IPR003340','IPR001471']
arfdomains_ap2b3pb1 = ['IPR001471','IPR003340','IPR000270']

# Empty lists to append the matched scaffolds
b3arfpb1 = []
b3arf = []
arfpb1 = []
b3pb1 = []
arfap2 = []
b3ap2 = []
ap2b3pb1 = []
remaining = []

# Add the matched scaffolds to those lists, respectively
for key in result:
    if set(arfdomains_all1).issubset(result[key]) or set(arfdomains_all2).issubset(result[key]):
        b3arfpb1.append(key)
    elif set(arfdomains_b3arf) == set(result[key]):
        b3arf.append(key)
    elif set(arfdomains_arfpb1) == set(result[key]) or set(arfdomains_arfauxiaa) == set(result[key]):
        arfpb1.append(key)
    elif set(arfdomains_b3pb1) == set(result[key]) or set(arfdomains_b3auxiaa) == set(result[key]):
        b3pb1.append(key)
    elif set(arfdomains_arfap2).issubset(result[key]) or set(arfdomains_arfap2) == set(result[key]):
        arfap2.append(key)
    elif set(arfdomains_b3ap2).issubset(result[key]) or set(arfdomains_b3ap2) == set(result[key]):
        b3ap2.append(key)
    elif set(arfdomains_ap2b3pb1).issubset(result[key]) or set(arfdomains_ap2b3pb1) == set(result[key]):
        ap2b3pb1.append(key)
    else:
        remaining.append[key]

# Print number of scaffolds in each domain combination
print "B3-ARF-PB1 =",len(b3arfpb1)
print "B3-ARF =",len(b3arf)
print "ARF-PB1 =",len(arfpb1)
print "B3-PB1 =",len(b3pb1)
print "ARF-AP2 containing =",len(arfap2)
print "B3-AP2 =",len(b3ap2)
print "AP2-B3-PB1 =",len(ap2b3pb1)
print "Remaining =",len(remaining)



