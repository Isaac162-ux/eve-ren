from pathlib import PurePosixPath
from .models import PatchProposal

class CodeAgent:
    BLOCKED = {".env",".git","id_rsa","secrets.json"}
    def propose(self, path: str, content: str) -> PatchProposal:
        normalized = str(PurePosixPath(path)).lstrip("/")
        if normalized.startswith(".git/") or normalized.split("/",1)[0] in self.BLOCKED:
            raise ValueError("Caminho protegido: proposta bloqueada.")
        if ".." in PurePosixPath(normalized).parts:
            raise ValueError("Path traversal não permitido.")
        return PatchProposal(path=normalized,summary=f"Proposta de alteração para {normalized}",content=content)
