from sqlalchemy.orm import Session
from models.interview import Transcript
from models.transcription import Transcript as TranscriptModel
import time

def sync_transcripts(db: Session, items: list[Transcript]):
    results = []
    for item in items:
        server_item = db.query(TranscriptModel).filter(TranscriptModel.uuid == item.uuid).first()

        if not server_item:
            # Data baru, simpan ke database
            new_transcript = TranscriptModel(
                uuid=item.uuid,
                speaker_id=item.speaker_id,
                text=item.text,
                updated_at=item.updated_at,
                sync_status="synced"  # Anggap sudah tersinkronisasi saat dibuat di server
            )
            db.add(new_transcript)
            results.append({"uuid": item.uuid, "status": "created"})
        else:
            # Data sudah ada, cek konflik timestamp
            if item.updated_at > server_item.updated_at:
                server_item.speaker_id = item.speaker_id
                server_item.text = item.text
                server_item.updated_at = item.updated_at
                results.append({"uuid": item.uuid, "status": "updated"})
            else:
                results.append({"uuid": item.uuid, "status": "conflict"})
    
    db.commit()
    return results
