Name:       libtasn1
Version:    4.13
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
%configure --disable-static
%make_build

%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/bin/asn1Coding
/usr/bin/asn1Decoding
/usr/bin/asn1Parser
/usr/include/libtasn1.h
/usr/lib64/libtasn1.la
/usr/lib64/libtasn1.so
/usr/lib64/libtasn1.so.6
/usr/lib64/libtasn1.so.6.5.5
/usr/lib64/pkgconfig/libtasn1.pc
/usr/share/info/libtasn1.info.gz
/usr/share/man/man1/asn1Coding.1.gz
/usr/share/man/man1/asn1Decoding.1.gz
/usr/share/man/man1/asn1Parser.1.gz
/usr/share/man/man3/asn1_array2tree.3.gz
/usr/share/man/man3/asn1_bit_der.3.gz
/usr/share/man/man3/asn1_check_version.3.gz
/usr/share/man/man3/asn1_copy_node.3.gz
/usr/share/man/man3/asn1_create_element.3.gz
/usr/share/man/man3/asn1_decode_simple_ber.3.gz
/usr/share/man/man3/asn1_decode_simple_der.3.gz
/usr/share/man/man3/asn1_delete_element.3.gz
/usr/share/man/man3/asn1_delete_structure.3.gz
/usr/share/man/man3/asn1_delete_structure2.3.gz
/usr/share/man/man3/asn1_der_coding.3.gz
/usr/share/man/man3/asn1_der_decoding.3.gz
/usr/share/man/man3/asn1_der_decoding2.3.gz
/usr/share/man/man3/asn1_der_decoding_element.3.gz
/usr/share/man/man3/asn1_der_decoding_startEnd.3.gz
/usr/share/man/man3/asn1_dup_node.3.gz
/usr/share/man/man3/asn1_encode_simple_der.3.gz
/usr/share/man/man3/asn1_expand_any_defined_by.3.gz
/usr/share/man/man3/asn1_expand_octet_string.3.gz
/usr/share/man/man3/asn1_find_node.3.gz
/usr/share/man/man3/asn1_find_structure_from_oid.3.gz
/usr/share/man/man3/asn1_get_bit_der.3.gz
/usr/share/man/man3/asn1_get_length_ber.3.gz
/usr/share/man/man3/asn1_get_length_der.3.gz
/usr/share/man/man3/asn1_get_object_id_der.3.gz
/usr/share/man/man3/asn1_get_octet_der.3.gz
/usr/share/man/man3/asn1_get_tag_der.3.gz
/usr/share/man/man3/asn1_length_der.3.gz
/usr/share/man/man3/asn1_number_of_elements.3.gz
/usr/share/man/man3/asn1_octet_der.3.gz
/usr/share/man/man3/asn1_parser2array.3.gz
/usr/share/man/man3/asn1_parser2tree.3.gz
/usr/share/man/man3/asn1_perror.3.gz
/usr/share/man/man3/asn1_print_structure.3.gz
/usr/share/man/man3/asn1_read_node_value.3.gz
/usr/share/man/man3/asn1_read_tag.3.gz
/usr/share/man/man3/asn1_read_value.3.gz
/usr/share/man/man3/asn1_read_value_type.3.gz
/usr/share/man/man3/asn1_strerror.3.gz
/usr/share/man/man3/asn1_write_value.3.gz

%changelog
# let's skip this for now
