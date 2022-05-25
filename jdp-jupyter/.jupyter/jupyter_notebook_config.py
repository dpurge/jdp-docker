c = get_config()
c.IPKernelApp.pylab = 'inline'
# c.NotebookApp.ip = '*'
c.NotebookApp.ip = '0.0.0.0'
c.NotebookApp.allow_remote_access = True
c.NotebookApp.open_browser = False
c.NotebookApp.token = ''
c.NotebookApp.notebook_dir = "/workspace"
c.NotebookApp.allow_root = True
c.NotebookApp.allow_origin = '*'
c.NotebookApp.tornado_settings = {
    'headers': {
        'Content-Security-Policy': "frame-ancestors 'self' *"
    }
}
