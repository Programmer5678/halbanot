from src.domain_error import DomainError


class NonDirectoryDE(DomainError):
    """Expected the docx dir to have subdirs only, found non-dir"""
    pass

class NonFileDE(DomainError):
    pass

