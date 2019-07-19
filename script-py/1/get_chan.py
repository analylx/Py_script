import paramiko
 
paramiko.util.log_to_file('/tmp/li.log')
ssh = paramiko.SSHClient()
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('172.30.126.31', port=22, username='root', password='hello')
channel = ssh.invoke_shell()  # 登录到远程主机，开一个终端
channel.close()
ssh.close()
 
 
def invoke_shell(self, term='vt100', width=80, height=24, width_pixels=0,
                 height_pixels=0):
    """
        Start an interactive shell session on the SSH server.  A new L{Channel}
        is opened and connected to a pseudo-terminal using the requested
        terminal type and size.
        @param term: the terminal type to emulate (for example, C{"vt100"})
        @type term: str
        @param width: the width (in characters) of the terminal window
        @type width: int
        @param height: the height (in characters) of the terminal window
        @type height: int
        @param width_pixels: the width (in pixels) of the terminal window
        @type width_pixels: int
        @param height_pixels: the height (in pixels) of the terminal window
        @type height_pixels: int
        @return: a new channel connected to the remote shell
        @rtype: L{Channel}
        @raise SSHException: if the server fails to invoke a shell
    """
        chan = self._transport.open_session()
        chan.get_pty(term, width, height, width_pixels, height_pixels)
        chan.invoke_shell()
        return chan
 
 
def invoke_shell(self):
    """
        Request an interactive shell session on this channel.  If the server
        allows it, the channel will then be directly connected to the stdin,
        stdout, and stderr of the shell.
        Normally you would call L{get_pty} before this, in which case the
        shell will operate through the pty, and the channel will be connected
        to the stdin and stdout of the pty.
        When the shell exits, the channel will be closed and can't be reused.
        You must open a new channel if you wish to open another shell.
        @raise SSHException: if the request was rejected or the channel was
            closed
    """
    if self.closed or self.eof_received or self.eof_sent or not self.active:
        raise SSHException('Channel is not open')
    m = Message()
    m.add_byte(chr(MSG_CHANNEL_REQUEST))
    m.add_int(self.remote_chanid)
    m.add_string('shell')
    m.add_boolean(1)
    self._event_pending()
    self.transport._send_user_message(m)
    self._wait_for_event()
