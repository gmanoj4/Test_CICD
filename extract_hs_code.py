# -*- coding: utf-8 -*-

import re

def extract_HS_Code(str):
    """Extract HS-code from google output
    and append zeros to make Fully Qualified HS-Code.
    """
    res = re.findall("HS Code\s(\d[0-9]*)",str)
    res.sort(key=len)
    res.reverse()
    HS = res[0]
    if len(HS)%2!=0:
        HS  = '0'+HS
    while len(HS) <14:
        HS = HS + "0"
    return HS
   
#string = "{'title': 'HS Code 0808 | Harmonized System Code of APPLES ...', 'link': 'http://www.cybex.in/HS-Codes/Apples-Pears-Quinces-Fresh-Heading-0808.aspx'} {'title': 'Import Data and Price of apple fruit under HS Code 08081000 ...', 'link': 'https://www.zauba.com/import-apple+fruit/hs-code-08081000-hs-code.html'} {'title': 'Import Data and Price of fresh fuji apple under HS Code 0808 ...', 'link': 'https://www.zauba.com/import-FRESH+FUJI+APPLE/hs-code-0808-hs-code.html'} {'title': 'Apple fruit HS Codes - Seair Exim Solutions', 'link': 'https://www.seair.co.in/apple-fruit-hs-code.aspx'} {'title': 'HS Code 080810 - Trade Statistics, Tariff Rates for Apples ...', 'link': 'https://www.flexport.com/data/hs-code/080810-apples-fresh'} {'title': 'HSN Code for Apple Fruit in India - Export Genius', 'link': 'https://www.exportgenius.in/hs-code/india/apple-fruit'} {'title': 'Legal - Global Trade Compliance - Apple', 'link': 'https://www.apple.com/in/legal/more-resources/gtc.html'} {'title': '08081000 - - Apples, pears and quinces, fresh ... - HS Code', 'link': 'https://www.exportimportstatistics.com/importers/08081000.aspx'} {'title': 'HS code for apples, pears and quinces, fresh', 'link': 'https://howtoexportimport.com/HS-code-for-apples-pears-and-quinces-fresh-2875.aspx'} {'title': 'HS Code 08133000 - Dried, apples - Tariff Number', 'link': 'https://www.tariffnumber.com/2020/08133000'}"

#print(Extract_HS_Code(string))
    
#print(extract_HS_Code.__doc__ )