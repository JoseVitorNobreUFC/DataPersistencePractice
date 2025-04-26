import os
import xml.etree.ElementTree as ET
from typing import List, Optional, Dict, Any

def read_xml(filename: str) -> List[Dict[str, Any]]:
    if not os.path.exists(filename):
        return []

    tree = ET.parse(filename)
    root = tree.getroot()
    return [
        {child.tag: child.text for child in record}
        for record in root.findall("record")
    ]

def write_xml(filename: str, data: List[Dict[str, Any]]):
    root = ET.Element("records")
    for record_data in data:
        record = ET.SubElement(root, "record")
        for key, value in record_data.items():
            field = ET.SubElement(record, key)
            field.text = str(value)
    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)

def get_next_id(filename: str) -> int:
    records = read_xml(filename)
    if not records:
        return 1
    ids = [int(record["id"]) for record in records if record["id"].isdigit()]
    return max(ids) + 1 if ids else 1

def create_record(filename: str, record: Dict[str, Any]):
    records = read_xml(filename)
    records.append(record)
    write_xml(filename, records)
    return records

def get_all_records(filename: str) -> List[Dict[str, Any]]:
    return read_xml(filename)

def get_record_by_id(filename: str, record_id: int) -> Optional[Dict[str, Any]]:
    records = read_xml(filename)
    for record in records:
        if int(record["id"]) == record_id:
            return record
    return None

def update_record(filename: str, record_id: int, updated_data: Dict[str, Any]):
    records = read_xml(filename)
    updated = False

    for i, record in enumerate(records):
        if int(record["id"]) == record_id:
            updated_record = {
                "id": str(record_id),
                **updated_data
            }
            records[i] = updated_record
            updated = True
            break

    if updated:
        write_xml(filename, records)
        return True
    return False

def delete_record(filename: str, record_id: int):
    records = read_xml(filename)
    filtered = [record for record in records if int(record["id"]) != record_id]
    if len(filtered) != len(records):
        write_xml(filename, filtered)
        return True
    return False
