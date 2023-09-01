Name:       libssh2
Version:    1.8.0
Release:    1
Summary:    TODO
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.gz


%description
TODO

%prep
%setup -a 0

%build
%configure --disable-static
%make_build

%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/include/libssh2.h
/usr/include/libssh2_publickey.h
/usr/include/libssh2_sftp.h
/usr/lib64/libssh2.so
/usr/lib64/libssh2.so.1
/usr/lib64/libssh2.so.1.0.1
/usr/lib64/pkgconfig/libssh2.pc
/usr/share/man/man3/libssh2_agent_connect.3.gz
/usr/share/man/man3/libssh2_agent_disconnect.3.gz
/usr/share/man/man3/libssh2_agent_free.3.gz
/usr/share/man/man3/libssh2_agent_get_identity.3.gz
/usr/share/man/man3/libssh2_agent_init.3.gz
/usr/share/man/man3/libssh2_agent_list_identities.3.gz
/usr/share/man/man3/libssh2_agent_userauth.3.gz
/usr/share/man/man3/libssh2_banner_set.3.gz
/usr/share/man/man3/libssh2_base64_decode.3.gz
/usr/share/man/man3/libssh2_channel_close.3.gz
/usr/share/man/man3/libssh2_channel_direct_tcpip.3.gz
/usr/share/man/man3/libssh2_channel_direct_tcpip_ex.3.gz
/usr/share/man/man3/libssh2_channel_eof.3.gz
/usr/share/man/man3/libssh2_channel_exec.3.gz
/usr/share/man/man3/libssh2_channel_flush.3.gz
/usr/share/man/man3/libssh2_channel_flush_ex.3.gz
/usr/share/man/man3/libssh2_channel_flush_stderr.3.gz
/usr/share/man/man3/libssh2_channel_forward_accept.3.gz
/usr/share/man/man3/libssh2_channel_forward_cancel.3.gz
/usr/share/man/man3/libssh2_channel_forward_listen.3.gz
/usr/share/man/man3/libssh2_channel_forward_listen_ex.3.gz
/usr/share/man/man3/libssh2_channel_free.3.gz
/usr/share/man/man3/libssh2_channel_get_exit_signal.3.gz
/usr/share/man/man3/libssh2_channel_get_exit_status.3.gz
/usr/share/man/man3/libssh2_channel_handle_extended_data.3.gz
/usr/share/man/man3/libssh2_channel_handle_extended_data2.3.gz
/usr/share/man/man3/libssh2_channel_ignore_extended_data.3.gz
/usr/share/man/man3/libssh2_channel_open_ex.3.gz
/usr/share/man/man3/libssh2_channel_open_session.3.gz
/usr/share/man/man3/libssh2_channel_process_startup.3.gz
/usr/share/man/man3/libssh2_channel_read.3.gz
/usr/share/man/man3/libssh2_channel_read_ex.3.gz
/usr/share/man/man3/libssh2_channel_read_stderr.3.gz
/usr/share/man/man3/libssh2_channel_receive_window_adjust.3.gz
/usr/share/man/man3/libssh2_channel_receive_window_adjust2.3.gz
/usr/share/man/man3/libssh2_channel_request_pty.3.gz
/usr/share/man/man3/libssh2_channel_request_pty_ex.3.gz
/usr/share/man/man3/libssh2_channel_request_pty_size.3.gz
/usr/share/man/man3/libssh2_channel_request_pty_size_ex.3.gz
/usr/share/man/man3/libssh2_channel_send_eof.3.gz
/usr/share/man/man3/libssh2_channel_set_blocking.3.gz
/usr/share/man/man3/libssh2_channel_setenv.3.gz
/usr/share/man/man3/libssh2_channel_setenv_ex.3.gz
/usr/share/man/man3/libssh2_channel_shell.3.gz
/usr/share/man/man3/libssh2_channel_subsystem.3.gz
/usr/share/man/man3/libssh2_channel_wait_closed.3.gz
/usr/share/man/man3/libssh2_channel_wait_eof.3.gz
/usr/share/man/man3/libssh2_channel_window_read.3.gz
/usr/share/man/man3/libssh2_channel_window_read_ex.3.gz
/usr/share/man/man3/libssh2_channel_window_write.3.gz
/usr/share/man/man3/libssh2_channel_window_write_ex.3.gz
/usr/share/man/man3/libssh2_channel_write.3.gz
/usr/share/man/man3/libssh2_channel_write_ex.3.gz
/usr/share/man/man3/libssh2_channel_write_stderr.3.gz
/usr/share/man/man3/libssh2_channel_x11_req.3.gz
/usr/share/man/man3/libssh2_channel_x11_req_ex.3.gz
/usr/share/man/man3/libssh2_exit.3.gz
/usr/share/man/man3/libssh2_free.3.gz
/usr/share/man/man3/libssh2_hostkey_hash.3.gz
/usr/share/man/man3/libssh2_init.3.gz
/usr/share/man/man3/libssh2_keepalive_config.3.gz
/usr/share/man/man3/libssh2_keepalive_send.3.gz
/usr/share/man/man3/libssh2_knownhost_add.3.gz
/usr/share/man/man3/libssh2_knownhost_addc.3.gz
/usr/share/man/man3/libssh2_knownhost_check.3.gz
/usr/share/man/man3/libssh2_knownhost_checkp.3.gz
/usr/share/man/man3/libssh2_knownhost_del.3.gz
/usr/share/man/man3/libssh2_knownhost_free.3.gz
/usr/share/man/man3/libssh2_knownhost_get.3.gz
/usr/share/man/man3/libssh2_knownhost_init.3.gz
/usr/share/man/man3/libssh2_knownhost_readfile.3.gz
/usr/share/man/man3/libssh2_knownhost_readline.3.gz
/usr/share/man/man3/libssh2_knownhost_writefile.3.gz
/usr/share/man/man3/libssh2_knownhost_writeline.3.gz
/usr/share/man/man3/libssh2_poll.3.gz
/usr/share/man/man3/libssh2_poll_channel_read.3.gz
/usr/share/man/man3/libssh2_publickey_add.3.gz
/usr/share/man/man3/libssh2_publickey_add_ex.3.gz
/usr/share/man/man3/libssh2_publickey_init.3.gz
/usr/share/man/man3/libssh2_publickey_list_fetch.3.gz
/usr/share/man/man3/libssh2_publickey_list_free.3.gz
/usr/share/man/man3/libssh2_publickey_remove.3.gz
/usr/share/man/man3/libssh2_publickey_remove_ex.3.gz
/usr/share/man/man3/libssh2_publickey_shutdown.3.gz
/usr/share/man/man3/libssh2_scp_recv.3.gz
/usr/share/man/man3/libssh2_scp_recv2.3.gz
/usr/share/man/man3/libssh2_scp_send.3.gz
/usr/share/man/man3/libssh2_scp_send64.3.gz
/usr/share/man/man3/libssh2_scp_send_ex.3.gz
/usr/share/man/man3/libssh2_session_abstract.3.gz
/usr/share/man/man3/libssh2_session_banner_get.3.gz
/usr/share/man/man3/libssh2_session_banner_set.3.gz
/usr/share/man/man3/libssh2_session_block_directions.3.gz
/usr/share/man/man3/libssh2_session_callback_set.3.gz
/usr/share/man/man3/libssh2_session_disconnect.3.gz
/usr/share/man/man3/libssh2_session_disconnect_ex.3.gz
/usr/share/man/man3/libssh2_session_flag.3.gz
/usr/share/man/man3/libssh2_session_free.3.gz
/usr/share/man/man3/libssh2_session_get_blocking.3.gz
/usr/share/man/man3/libssh2_session_get_timeout.3.gz
/usr/share/man/man3/libssh2_session_handshake.3.gz
/usr/share/man/man3/libssh2_session_hostkey.3.gz
/usr/share/man/man3/libssh2_session_init.3.gz
/usr/share/man/man3/libssh2_session_init_ex.3.gz
/usr/share/man/man3/libssh2_session_last_errno.3.gz
/usr/share/man/man3/libssh2_session_last_error.3.gz
/usr/share/man/man3/libssh2_session_method_pref.3.gz
/usr/share/man/man3/libssh2_session_methods.3.gz
/usr/share/man/man3/libssh2_session_set_blocking.3.gz
/usr/share/man/man3/libssh2_session_set_last_error.3.gz
/usr/share/man/man3/libssh2_session_set_timeout.3.gz
/usr/share/man/man3/libssh2_session_startup.3.gz
/usr/share/man/man3/libssh2_session_supported_algs.3.gz
/usr/share/man/man3/libssh2_sftp_close.3.gz
/usr/share/man/man3/libssh2_sftp_close_handle.3.gz
/usr/share/man/man3/libssh2_sftp_closedir.3.gz
/usr/share/man/man3/libssh2_sftp_fsetstat.3.gz
/usr/share/man/man3/libssh2_sftp_fstat.3.gz
/usr/share/man/man3/libssh2_sftp_fstat_ex.3.gz
/usr/share/man/man3/libssh2_sftp_fstatvfs.3.gz
/usr/share/man/man3/libssh2_sftp_fsync.3.gz
/usr/share/man/man3/libssh2_sftp_get_channel.3.gz
/usr/share/man/man3/libssh2_sftp_init.3.gz
/usr/share/man/man3/libssh2_sftp_last_error.3.gz
/usr/share/man/man3/libssh2_sftp_lstat.3.gz
/usr/share/man/man3/libssh2_sftp_mkdir.3.gz
/usr/share/man/man3/libssh2_sftp_mkdir_ex.3.gz
/usr/share/man/man3/libssh2_sftp_open.3.gz
/usr/share/man/man3/libssh2_sftp_open_ex.3.gz
/usr/share/man/man3/libssh2_sftp_opendir.3.gz
/usr/share/man/man3/libssh2_sftp_read.3.gz
/usr/share/man/man3/libssh2_sftp_readdir.3.gz
/usr/share/man/man3/libssh2_sftp_readdir_ex.3.gz
/usr/share/man/man3/libssh2_sftp_readlink.3.gz
/usr/share/man/man3/libssh2_sftp_realpath.3.gz
/usr/share/man/man3/libssh2_sftp_rename.3.gz
/usr/share/man/man3/libssh2_sftp_rename_ex.3.gz
/usr/share/man/man3/libssh2_sftp_rewind.3.gz
/usr/share/man/man3/libssh2_sftp_rmdir.3.gz
/usr/share/man/man3/libssh2_sftp_rmdir_ex.3.gz
/usr/share/man/man3/libssh2_sftp_seek.3.gz
/usr/share/man/man3/libssh2_sftp_seek64.3.gz
/usr/share/man/man3/libssh2_sftp_setstat.3.gz
/usr/share/man/man3/libssh2_sftp_shutdown.3.gz
/usr/share/man/man3/libssh2_sftp_stat.3.gz
/usr/share/man/man3/libssh2_sftp_stat_ex.3.gz
/usr/share/man/man3/libssh2_sftp_statvfs.3.gz
/usr/share/man/man3/libssh2_sftp_symlink.3.gz
/usr/share/man/man3/libssh2_sftp_symlink_ex.3.gz
/usr/share/man/man3/libssh2_sftp_tell.3.gz
/usr/share/man/man3/libssh2_sftp_tell64.3.gz
/usr/share/man/man3/libssh2_sftp_unlink.3.gz
/usr/share/man/man3/libssh2_sftp_unlink_ex.3.gz
/usr/share/man/man3/libssh2_sftp_write.3.gz
/usr/share/man/man3/libssh2_trace.3.gz
/usr/share/man/man3/libssh2_trace_sethandler.3.gz
/usr/share/man/man3/libssh2_userauth_authenticated.3.gz
/usr/share/man/man3/libssh2_userauth_hostbased_fromfile.3.gz
/usr/share/man/man3/libssh2_userauth_hostbased_fromfile_ex.3.gz
/usr/share/man/man3/libssh2_userauth_keyboard_interactive.3.gz
/usr/share/man/man3/libssh2_userauth_keyboard_interactive_ex.3.gz
/usr/share/man/man3/libssh2_userauth_list.3.gz
/usr/share/man/man3/libssh2_userauth_password.3.gz
/usr/share/man/man3/libssh2_userauth_password_ex.3.gz
/usr/share/man/man3/libssh2_userauth_publickey.3.gz
/usr/share/man/man3/libssh2_userauth_publickey_fromfile.3.gz
/usr/share/man/man3/libssh2_userauth_publickey_fromfile_ex.3.gz
/usr/share/man/man3/libssh2_userauth_publickey_frommemory.3.gz
/usr/share/man/man3/libssh2_version.3.gz

%changelog
# let's skip this for now

