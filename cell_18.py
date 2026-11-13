# ZIP all computed results
import shutil
archive=shutil.make_archive(str(OUT),'zip',root_dir=str(OUT))
print('Created:',archive)
