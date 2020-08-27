FROM centos:8

ARG USERID
ENV USERID $USERID

# Install main dependencies
RUN yum install -y epel-release rpmdevtools make yum-utils '@Development Tools' \
    python3-devel python3-setuptools && \
    yum clean all

# Create builder group and user
RUN groupadd -g $USERID builder && \
    useradd -m -s /bin/bash -u $USERID -g $USERID builder

USER builder
RUN rpmdev-setuptree
WORKDIR /home/builder/rpmbuild
VOLUME [ "/host" ]
CMD rpmbuild -ba
