#!/usr/bin/env python3
"""Restituer les deux originaux volumineux, après clonage complet du dépôt."""
from pathlib import Path
import argparse,gzip,hashlib,json

def restore(root,dest):
    inventory=json.loads((root/'sources/inventaire-integration-chatgpt-2026-11-04.json').read_text())
    for item in inventory['files']:
        if item.get('original_archive'):
            blob=gzip.decompress((root/item['original_archive']).read_bytes())
            target=dest/Path(item['path']).name
            expected=item['original_sha256']
        elif item.get('restore_manifest'):
            meta=json.loads((root/item['restore_manifest']).read_text())
            chunks=[]
            for part in meta['parts']:
                b=(root/part['path']).read_bytes()
                assert len(b)==part['bytes'] and hashlib.sha256(b).hexdigest()==part['sha256'],part['path']
                chunks.append(b)
            blob=b''.join(chunks);expected=meta['original_sha256']
            assert len(blob)==meta['original_bytes']
            target=dest/Path(meta['original_path']).name
        else:
            continue
        assert hashlib.sha256(blob).hexdigest()==expected,str(target)
        dest.mkdir(parents=True,exist_ok=True)
        with target.open('xb') as f:f.write(blob)
        print(f'OK {target.name} ({len(blob)} octets)')

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--sortie',type=Path,required=True)
    args=p.parse_args()
    restore(Path(__file__).resolve().parents[1],args.sortie)
