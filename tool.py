"""Validate changelog fragment names and descriptions."""
from __future__ import annotations
from pathlib import Path
def validate(filename:str,text:str,categories:list[str])->list[str]:
 errors=[];parts=Path(filename).name.split('.')
 if len(parts)!=3 or parts[1] not in categories:errors.append('invalid filename category')
 if not text.strip():errors.append('empty description')
 if len(text.strip())>280:errors.append('description too long')
 return errors
def check(fragments:list[dict],categories:list[str])->dict:return {item['filename']:validate(item['filename'],item.get('text',''),categories) for item in fragments}
if __name__=='__main__':
 import json,sys;p=json.load(sys.stdin);print(json.dumps(check(p['fragments'],p['categories']),indent=2,sort_keys=True))
