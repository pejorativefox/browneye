FROM scratch
ADD build/browneye-rootfs.tar.gz /
RUN mkdir /build
WORKDIR /build
CMD ["/bin/bash"]

