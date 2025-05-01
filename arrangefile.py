from pathlib import Path
import shutil

# Define your categorized extension lists
document_extensions = [
    "txt", "doc", "docx", "rtf", "odt", "ppt", "pptx", "pps", "pub"
]
xldocument_extensions = [
    "csv", "xls", "xlsx"
]
pdfdocument_extensions = [
    "pdf" 
]
image_extensions = [
    "jpg", "jpeg", "png", "gif", "bmp", "tif", "tiff", "ico", "svg", "psd", "ai", "eps", "webp", "raw"
]
audio_extensions = [
    "mp3", "wav", "wma", "aac", "flac", "ogg", "m4a", "mid", "aiff", "au", "cda"
]
video_extensions = [
    "mp4", "avi", "mov", "wmv", "flv", "mkv", "mpeg", "mpg", "3gp", "webm", "vob", "m4v"
]
archive_extensions = [
    "zip", "rar", "7z", "tar", "gz", "bz2", "xz", "iso", "dmg", "cab", "tgz", "jar", "lzh", "sitx", "z"
]
executable_extensions = [
    "exe", "msi", "bat", "sh", "bin", "dll", "sys", "com", "cmd", "scr", "vbs"
]
web_extensions = [
    "html", "htm", "xml", "xhtml", "css", "js", "php", "asp", "aspx", "jsp", "json", "rss", "xsl"
]
database_extensions = [
    "db", "mdb", "accdb", "sqlite", "sql", "dbf", "ndf", "ora"
]
email_extensions = [
    "eml", "msg", "ics", "vcf", "pst", "ost"
]
misc_extensions = [
    "ini", "cfg", "conf", "log", "bak", "tmp", "swp", "dat", "lst", "lock"
]
programming_extensions = [
    "py", "java", "c", "cpp", "h", "cs", "rb", "pl", "pm", "sh", "bash", "ps1", "go", "swift", "kt",
    "php3", "php4", "php5", "phtml", "asm", "class", "vb"
]
specialized_extensions = [
    "ps", "eps", "dxf", "dwg", "stl", "obj", "3ds", "fbx", "glb", "gltf", "dae", "blend", "skp"
]
other_extensions = [
    "shtml", "shtm", "xsd", "yml", "yaml", "toml", "md", "rst", "tex", "latex", "bak", "old", "orig"
]
case_variants = [
    "TXT", "JPG", "GIF", "ZIP", "DOC", "LOG", "PNG", "HTML", "MP3"
]

# Map category names to their extension lists (all lowercase)
categories = {
    "Document": set(ext.lower() for ext in document_extensions),
    "Excel": set(ext.lower() for ext in xldocument_extensions),
    "PDF": set(ext.lower() for ext in pdfdocument_extensions),
    "Image": set(ext.lower() for ext in image_extensions),
    "Audio": set(ext.lower() for ext in audio_extensions),
    "Video": set(ext.lower() for ext in video_extensions),
    "Archive": set(ext.lower() for ext in archive_extensions),
    "Executable": set(ext.lower() for ext in executable_extensions),
    "Web": set(ext.lower() for ext in web_extensions),
    "Database": set(ext.lower() for ext in database_extensions),
    "Email": set(ext.lower() for ext in email_extensions),
    "Misc": set(ext.lower() for ext in misc_extensions),
    "Programming": set(ext.lower() for ext in programming_extensions),
    "Specialized": set(ext.lower() for ext in specialized_extensions),
    "Other": set(ext.lower() for ext in other_extensions),
    "Case_variants": set(ext.lower() for ext in case_variants),
}

def get_category_for_extension(ext):
    """Return the category name for the given extension, or None if not found."""
    ext = ext.lower()
    for category, extensions in categories.items():
        if ext in extensions:
            return category
    return None

def move_files_by_extension(folder_path):
    folder = Path(folder_path)
    if not folder.is_dir():
        print(f"Error: {folder_path} is not a valid directory.")
        return

    for file in folder.iterdir():
        if file.is_file():
            ext = file.suffix[1:]  # Remove leading dot
            if not ext:
                continue  # Skip files without extension
            category = get_category_for_extension(ext)
            if category:
                target_folder = folder / category
                if not target_folder.exists():
                    target_folder.mkdir()
                # Move the file
                destination = target_folder / file.name
                # If a file with the same name exists, you might want to handle it (e.g., rename)
                if destination.exists():
                    print(f"Warning: {destination} already exists. Skipping {file.name}")
                    continue
                shutil.move(str(file), str(destination))
                print(f"Moved {file.name} to {category}/")

# Example usage:
if __name__ == "__main__":
    user_input = input("Paste your folder path: ").strip()
    folder_to_organize = Path(user_input).expanduser().resolve()
    move_files_by_extension(folder_to_organize)

