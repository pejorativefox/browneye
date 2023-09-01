Name:       libvorbis
Version:    1.3.6
Release:    1
Summary:    TODO
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.xz


%description
TODO

%prep
%setup -a 0 

%build
%configure  --disable-static
%make_build

%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/include/vorbis/codec.h
/usr/include/vorbis/vorbisenc.h
/usr/include/vorbis/vorbisfile.h
/usr/lib64/libvorbis.so
/usr/lib64/libvorbis.so.0
/usr/lib64/libvorbis.so.0.4.8
/usr/lib64/libvorbisenc.so
/usr/lib64/libvorbisenc.so.2
/usr/lib64/libvorbisenc.so.2.0.11
/usr/lib64/libvorbisfile.so
/usr/lib64/libvorbisfile.so.3
/usr/lib64/libvorbisfile.so.3.3.7
/usr/lib64/pkgconfig/vorbis.pc
/usr/lib64/pkgconfig/vorbisenc.pc
/usr/lib64/pkgconfig/vorbisfile.pc
/usr/share/aclocal/vorbis.m4
/usr/share/doc/libvorbis-1.3.6/doxygen-build.stamp
/usr/share/doc/libvorbis-1.3.6/eightphase.png
/usr/share/doc/libvorbis-1.3.6/fish_xiph_org.png
/usr/share/doc/libvorbis-1.3.6/floor1_inverse_dB_table.html
/usr/share/doc/libvorbis-1.3.6/floorval.png
/usr/share/doc/libvorbis-1.3.6/fourphase.png
/usr/share/doc/libvorbis-1.3.6/framing.html
/usr/share/doc/libvorbis-1.3.6/helper.html
/usr/share/doc/libvorbis-1.3.6/index.html
/usr/share/doc/libvorbis-1.3.6/libvorbis/index.html
/usr/share/doc/libvorbis-1.3.6/libvorbis/overview.html
/usr/share/doc/libvorbis-1.3.6/libvorbis/reference.html
/usr/share/doc/libvorbis-1.3.6/libvorbis/return.html
/usr/share/doc/libvorbis-1.3.6/libvorbis/style.css
/usr/share/doc/libvorbis-1.3.6/libvorbis/vorbis_analysis.html
/usr/share/doc/libvorbis-1.3.6/libvorbis/vorbis_analysis_blockout.html
/usr/share/doc/libvorbis-1.3.6/libvorbis/vorbis_analysis_buffer.html
/usr/share/doc/libvorbis-1.3.6/libvorbis/vorbis_analysis_headerout.html
/usr/share/doc/libvorbis-1.3.6/libvorbis/vorbis_analysis_init.html
/usr/share/doc/libvorbis-1.3.6/libvorbis/vorbis_analysis_wrote.html
/usr/share/doc/libvorbis-1.3.6/libvorbis/vorbis_bitrate_addblock.html
/usr/share/doc/libvorbis-1.3.6/libvorbis/vorbis_bitrate_flushpacket.html
/usr/share/doc/libvorbis-1.3.6/libvorbis/vorbis_block.html
/usr/share/doc/libvorbis-1.3.6/libvorbis/vorbis_block_clear.html
/usr/share/doc/libvorbis-1.3.6/libvorbis/vorbis_block_init.html
/usr/share/doc/libvorbis-1.3.6/libvorbis/vorbis_comment.html
/usr/share/doc/libvorbis-1.3.6/libvorbis/vorbis_comment_add.html
/usr/share/doc/libvorbis-1.3.6/libvorbis/vorbis_comment_add_tag.html
/usr/share/doc/libvorbis-1.3.6/libvorbis/vorbis_comment_clear.html
/usr/share/doc/libvorbis-1.3.6/libvorbis/vorbis_comment_init.html
/usr/share/doc/libvorbis-1.3.6/libvorbis/vorbis_comment_query.html
/usr/share/doc/libvorbis-1.3.6/libvorbis/vorbis_comment_query_count.html
/usr/share/doc/libvorbis-1.3.6/libvorbis/vorbis_commentheader_out.html
/usr/share/doc/libvorbis-1.3.6/libvorbis/vorbis_dsp_clear.html
/usr/share/doc/libvorbis-1.3.6/libvorbis/vorbis_dsp_state.html
/usr/share/doc/libvorbis-1.3.6/libvorbis/vorbis_granule_time.html
/usr/share/doc/libvorbis-1.3.6/libvorbis/vorbis_info.html
/usr/share/doc/libvorbis-1.3.6/libvorbis/vorbis_info_blocksize.html
/usr/share/doc/libvorbis-1.3.6/libvorbis/vorbis_info_clear.html
/usr/share/doc/libvorbis-1.3.6/libvorbis/vorbis_info_init.html
/usr/share/doc/libvorbis-1.3.6/libvorbis/vorbis_packet_blocksize.html
/usr/share/doc/libvorbis-1.3.6/libvorbis/vorbis_synthesis.html
/usr/share/doc/libvorbis-1.3.6/libvorbis/vorbis_synthesis_blockin.html
/usr/share/doc/libvorbis-1.3.6/libvorbis/vorbis_synthesis_halfrate.html
/usr/share/doc/libvorbis-1.3.6/libvorbis/vorbis_synthesis_halfrate_p.html
/usr/share/doc/libvorbis-1.3.6/libvorbis/vorbis_synthesis_headerin.html
/usr/share/doc/libvorbis-1.3.6/libvorbis/vorbis_synthesis_idheader.html
/usr/share/doc/libvorbis-1.3.6/libvorbis/vorbis_synthesis_init.html
/usr/share/doc/libvorbis-1.3.6/libvorbis/vorbis_synthesis_lapout.html
/usr/share/doc/libvorbis-1.3.6/libvorbis/vorbis_synthesis_pcmout.html
/usr/share/doc/libvorbis-1.3.6/libvorbis/vorbis_synthesis_read.html
/usr/share/doc/libvorbis-1.3.6/libvorbis/vorbis_synthesis_restart.html
/usr/share/doc/libvorbis-1.3.6/libvorbis/vorbis_synthesis_trackonly.html
/usr/share/doc/libvorbis-1.3.6/libvorbis/vorbis_version_string.html
/usr/share/doc/libvorbis-1.3.6/oggstream.html
/usr/share/doc/libvorbis-1.3.6/programming.html
/usr/share/doc/libvorbis-1.3.6/rfc5215.txt
/usr/share/doc/libvorbis-1.3.6/rfc5215.xml
/usr/share/doc/libvorbis-1.3.6/squarepolar.png
/usr/share/doc/libvorbis-1.3.6/stereo.html
/usr/share/doc/libvorbis-1.3.6/stream.png
/usr/share/doc/libvorbis-1.3.6/v-comment.html
/usr/share/doc/libvorbis-1.3.6/vorbis-clip.txt
/usr/share/doc/libvorbis-1.3.6/vorbis-errors.txt
/usr/share/doc/libvorbis-1.3.6/vorbis-fidelity.html
/usr/share/doc/libvorbis-1.3.6/vorbisenc/changes.html
/usr/share/doc/libvorbis-1.3.6/vorbisenc/examples.html
/usr/share/doc/libvorbis-1.3.6/vorbisenc/index.html
/usr/share/doc/libvorbis-1.3.6/vorbisenc/ovectl_ratemanage2_arg.html
/usr/share/doc/libvorbis-1.3.6/vorbisenc/ovectl_ratemanage_arg.html
/usr/share/doc/libvorbis-1.3.6/vorbisenc/overview.html
/usr/share/doc/libvorbis-1.3.6/vorbisenc/reference.html
/usr/share/doc/libvorbis-1.3.6/vorbisenc/style.css
/usr/share/doc/libvorbis-1.3.6/vorbisenc/vorbis_encode_ctl.html
/usr/share/doc/libvorbis-1.3.6/vorbisenc/vorbis_encode_init.html
/usr/share/doc/libvorbis-1.3.6/vorbisenc/vorbis_encode_init_vbr.html
/usr/share/doc/libvorbis-1.3.6/vorbisenc/vorbis_encode_setup_init.html
/usr/share/doc/libvorbis-1.3.6/vorbisenc/vorbis_encode_setup_managed.html
/usr/share/doc/libvorbis-1.3.6/vorbisenc/vorbis_encode_setup_vbr.html
/usr/share/doc/libvorbis-1.3.6/vorbisfile/OggVorbis_File.html
/usr/share/doc/libvorbis-1.3.6/vorbisfile/callbacks.html
/usr/share/doc/libvorbis-1.3.6/vorbisfile/chaining_example_c.html
/usr/share/doc/libvorbis-1.3.6/vorbisfile/chainingexample.html
/usr/share/doc/libvorbis-1.3.6/vorbisfile/crosslap.html
/usr/share/doc/libvorbis-1.3.6/vorbisfile/datastructures.html
/usr/share/doc/libvorbis-1.3.6/vorbisfile/decoding.html
/usr/share/doc/libvorbis-1.3.6/vorbisfile/example.html
/usr/share/doc/libvorbis-1.3.6/vorbisfile/exampleindex.html
/usr/share/doc/libvorbis-1.3.6/vorbisfile/fileinfo.html
/usr/share/doc/libvorbis-1.3.6/vorbisfile/index.html
/usr/share/doc/libvorbis-1.3.6/vorbisfile/initialization.html
/usr/share/doc/libvorbis-1.3.6/vorbisfile/ov_bitrate.html
/usr/share/doc/libvorbis-1.3.6/vorbisfile/ov_bitrate_instant.html
/usr/share/doc/libvorbis-1.3.6/vorbisfile/ov_callbacks.html
/usr/share/doc/libvorbis-1.3.6/vorbisfile/ov_clear.html
/usr/share/doc/libvorbis-1.3.6/vorbisfile/ov_comment.html
/usr/share/doc/libvorbis-1.3.6/vorbisfile/ov_crosslap.html
/usr/share/doc/libvorbis-1.3.6/vorbisfile/ov_fopen.html
/usr/share/doc/libvorbis-1.3.6/vorbisfile/ov_info.html
/usr/share/doc/libvorbis-1.3.6/vorbisfile/ov_open.html
/usr/share/doc/libvorbis-1.3.6/vorbisfile/ov_open_callbacks.html
/usr/share/doc/libvorbis-1.3.6/vorbisfile/ov_pcm_seek.html
/usr/share/doc/libvorbis-1.3.6/vorbisfile/ov_pcm_seek_lap.html
/usr/share/doc/libvorbis-1.3.6/vorbisfile/ov_pcm_seek_page.html
/usr/share/doc/libvorbis-1.3.6/vorbisfile/ov_pcm_seek_page_lap.html
/usr/share/doc/libvorbis-1.3.6/vorbisfile/ov_pcm_tell.html
/usr/share/doc/libvorbis-1.3.6/vorbisfile/ov_pcm_total.html
/usr/share/doc/libvorbis-1.3.6/vorbisfile/ov_raw_seek.html
/usr/share/doc/libvorbis-1.3.6/vorbisfile/ov_raw_seek_lap.html
/usr/share/doc/libvorbis-1.3.6/vorbisfile/ov_raw_tell.html
/usr/share/doc/libvorbis-1.3.6/vorbisfile/ov_raw_total.html
/usr/share/doc/libvorbis-1.3.6/vorbisfile/ov_read.html
/usr/share/doc/libvorbis-1.3.6/vorbisfile/ov_read_filter.html
/usr/share/doc/libvorbis-1.3.6/vorbisfile/ov_read_float.html
/usr/share/doc/libvorbis-1.3.6/vorbisfile/ov_seekable.html
/usr/share/doc/libvorbis-1.3.6/vorbisfile/ov_serialnumber.html
/usr/share/doc/libvorbis-1.3.6/vorbisfile/ov_streams.html
/usr/share/doc/libvorbis-1.3.6/vorbisfile/ov_test.html
/usr/share/doc/libvorbis-1.3.6/vorbisfile/ov_test_callbacks.html
/usr/share/doc/libvorbis-1.3.6/vorbisfile/ov_test_open.html
/usr/share/doc/libvorbis-1.3.6/vorbisfile/ov_time_seek.html
/usr/share/doc/libvorbis-1.3.6/vorbisfile/ov_time_seek_lap.html
/usr/share/doc/libvorbis-1.3.6/vorbisfile/ov_time_seek_page.html
/usr/share/doc/libvorbis-1.3.6/vorbisfile/ov_time_seek_page_lap.html
/usr/share/doc/libvorbis-1.3.6/vorbisfile/ov_time_tell.html
/usr/share/doc/libvorbis-1.3.6/vorbisfile/ov_time_total.html
/usr/share/doc/libvorbis-1.3.6/vorbisfile/overview.html
/usr/share/doc/libvorbis-1.3.6/vorbisfile/reference.html
/usr/share/doc/libvorbis-1.3.6/vorbisfile/seekexample.html
/usr/share/doc/libvorbis-1.3.6/vorbisfile/seeking.html
/usr/share/doc/libvorbis-1.3.6/vorbisfile/seeking_example_c.html
/usr/share/doc/libvorbis-1.3.6/vorbisfile/seeking_test_c.html
/usr/share/doc/libvorbis-1.3.6/vorbisfile/seekingexample.html
/usr/share/doc/libvorbis-1.3.6/vorbisfile/style.css
/usr/share/doc/libvorbis-1.3.6/vorbisfile/threads.html
/usr/share/doc/libvorbis-1.3.6/vorbisfile/vorbisfile_example_c.html

%changelog
# let's skip this for now

