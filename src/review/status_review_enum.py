from enum import StrEnum


class ReviewStatus(StrEnum):
    PUBLISHED = "PUBLISHED"
    DRAFT = "DRAFT"
    ARCHIVED = "ARCHIVED"