FROM scratch
ADD build/browneye-rootfs.tar.gz /
CMD ["/bin/bash"]

