Name:       libpipeline
Version:    1.5.1
Release:    1
Summary:    TODO
License:    GPL3
Source0:    %{name}-%{version}.tar.gz
Prefix:     /usr

%description
TODO

%prep
%setup -q -a0

%build
%configure 
%make_build

%install
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/include/pipeline.h
/usr/lib64/libpipeline.so
/usr/lib64/libpipeline.so.1
/usr/lib64/libpipeline.so.1.5.1
/usr/lib64/pkgconfig/libpipeline.pc
/usr/share/man/man3/libpipeline.3.gz
/usr/share/man/man3/pipecmd_arg.3.gz
/usr/share/man/man3/pipecmd_argf.3.gz
/usr/share/man/man3/pipecmd_args.3.gz
/usr/share/man/man3/pipecmd_argstr.3.gz
/usr/share/man/man3/pipecmd_argv.3.gz
/usr/share/man/man3/pipecmd_chdir.3.gz
/usr/share/man/man3/pipecmd_clearenv.3.gz
/usr/share/man/man3/pipecmd_discard_err.3.gz
/usr/share/man/man3/pipecmd_dump.3.gz
/usr/share/man/man3/pipecmd_dup.3.gz
/usr/share/man/man3/pipecmd_exec.3.gz
/usr/share/man/man3/pipecmd_fchdir.3.gz
/usr/share/man/man3/pipecmd_free.3.gz
/usr/share/man/man3/pipecmd_get_nargs.3.gz
/usr/share/man/man3/pipecmd_new.3.gz
/usr/share/man/man3/pipecmd_new_args.3.gz
/usr/share/man/man3/pipecmd_new_argstr.3.gz
/usr/share/man/man3/pipecmd_new_argv.3.gz
/usr/share/man/man3/pipecmd_new_function.3.gz
/usr/share/man/man3/pipecmd_new_passthrough.3.gz
/usr/share/man/man3/pipecmd_new_sequence.3.gz
/usr/share/man/man3/pipecmd_new_sequencev.3.gz
/usr/share/man/man3/pipecmd_nice.3.gz
/usr/share/man/man3/pipecmd_pre_exec.3.gz
/usr/share/man/man3/pipecmd_sequence_command.3.gz
/usr/share/man/man3/pipecmd_setenv.3.gz
/usr/share/man/man3/pipecmd_tostring.3.gz
/usr/share/man/man3/pipecmd_unsetenv.3.gz
/usr/share/man/man3/pipeline_command.3.gz
/usr/share/man/man3/pipeline_command_args.3.gz
/usr/share/man/man3/pipeline_command_argstr.3.gz
/usr/share/man/man3/pipeline_command_argv.3.gz
/usr/share/man/man3/pipeline_commands.3.gz
/usr/share/man/man3/pipeline_commandv.3.gz
/usr/share/man/man3/pipeline_connect.3.gz
/usr/share/man/man3/pipeline_dump.3.gz
/usr/share/man/man3/pipeline_free.3.gz
/usr/share/man/man3/pipeline_get_command.3.gz
/usr/share/man/man3/pipeline_get_infile.3.gz
/usr/share/man/man3/pipeline_get_ncommands.3.gz
/usr/share/man/man3/pipeline_get_outfile.3.gz
/usr/share/man/man3/pipeline_get_pid.3.gz
/usr/share/man/man3/pipeline_ignore_signals.3.gz
/usr/share/man/man3/pipeline_install_post_fork.3.gz
/usr/share/man/man3/pipeline_join.3.gz
/usr/share/man/man3/pipeline_new.3.gz
/usr/share/man/man3/pipeline_new_command_args.3.gz
/usr/share/man/man3/pipeline_new_command_argv.3.gz
/usr/share/man/man3/pipeline_new_commands.3.gz
/usr/share/man/man3/pipeline_new_commandv.3.gz
/usr/share/man/man3/pipeline_peek.3.gz
/usr/share/man/man3/pipeline_peek_size.3.gz
/usr/share/man/man3/pipeline_peek_skip.3.gz
/usr/share/man/man3/pipeline_peekline.3.gz
/usr/share/man/man3/pipeline_pump.3.gz
/usr/share/man/man3/pipeline_read.3.gz
/usr/share/man/man3/pipeline_readline.3.gz
/usr/share/man/man3/pipeline_run.3.gz
/usr/share/man/man3/pipeline_set_command.3.gz
/usr/share/man/man3/pipeline_start.3.gz
/usr/share/man/man3/pipeline_tostring.3.gz
/usr/share/man/man3/pipeline_wait.3.gz
/usr/share/man/man3/pipeline_wait_all.3.gz
/usr/share/man/man3/pipeline_want_in.3.gz
/usr/share/man/man3/pipeline_want_infile.3.gz
/usr/share/man/man3/pipeline_want_out.3.gz
/usr/share/man/man3/pipeline_want_outfile.3.gz

%changelog
# let's skip this for now
