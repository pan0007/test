Name: a
Version: a
Release: a
Summary: a
Source: a-a.tar.gz
License: a
Requires:	gcc
Requires:	kernel-headers
Requires:	perl-devel
Requires:	rubypick
Requires:	libdb-devel
Requires:	binutils
Requires:	rpm-devel
Requires:	xz-devel
Requires:	zlib-devel
Requires:	swig
Requires:	make
Requires:	expat-devel
Requires:	python3-devel
Requires:	gcc-c++
Requires:	python3
Requires:	glibc-headers
Requires:	ruby-devel
Requires:	perl
BuildRequires:	perl-devel
BuildRequires:	kernel-headers
BuildRequires:	rubypick
BuildRequires:	binutils
BuildRequires:	make
BuildRequires:	perl
BuildRequires:	rpm-devel
BuildRequires:	zlib-devel
BuildRequires:	swig
BuildRequires:	expat-devel
BuildRequires:	python3-devel
BuildRequires:	cmake
BuildRequires:	python3
BuildRequires:	glibc-headers
BuildRequires:	libdb-devel
BuildRequires:	xz-devel
BuildRequires:	gcc-c++
BuildRequires:	ruby-devel
BuildRequires:	gcc
%description
a

%prep
%autosetup

%build
cmake . -DCMAKE_BUILD_TYPE=RelWithDebInfo -DENABLE_PERL=1 -DENABLE_PYTHON=1 -DENABLE_RUBY=1 -DUSE_VENDORDIRS=1 -DFEDORA=1 -DENABLE_LZMA_COMPRESSION=1
%{make_build}

%install
make install DESTDIR="$RPM_BUILD_ROOT"

%check
make test ARGS='-V %{?_smp_mflags}'

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
/usr/local/share/man/man1/rpmdb2solv.1
/usr/local/include/solv/problems.h
/usr/local/bin/solv
/usr/local/include/solv/repodata.h
/usr/local/include/solv/testcase.h
/usr/local/include/solv/policy.h
/usr/lib64/python3.4/site-packages/__pycache__/solv.cpython-34.pyo
/usr/local/include/solv/poolarch.h
/usr/local/include/solv/repo_rpmdb.h
/usr/local/lib64/libsolv.so.0
/usr/local/share/man/man1/updateinfoxml2solv.1
/usr/local/bin/installcheck
/usr/local/include/solv/repo_rpmmd.h
/usr/local/bin/repomdxml2solv
/usr/local/include/solv/knownid.h
/usr/local/bin/testsolv
/usr/local/include/solv/evr.h
/usr/local/include/solv/solvable.h
/usr/lib64/python3.4/site-packages/_solv.so
/usr/local/include/solv/repo_updateinfoxml.h
/usr/lib64/perl5/vendor_perl/solv.so
/usr/local/include/solv/solvversion.h
/usr/local/share/man/man1/testsolv.1
/usr/lib64/ruby/vendor_ruby/solv.so
/usr/local/include/solv/rules.h
/usr/local/share/man/man1/installcheck.1
/usr/local/include/solv/solv_xfopen.h
/usr/lib64/perl5/vendor_perl/solv.pm
/usr/local/bin/rpmmd2solv
/usr/local/include/solv/util.h
/usr/local/share/man/man1/mergesolv.1
/usr/local/include/solv/transaction.h
/usr/local/share/man/man3/libsolv.3
/usr/local/bin/deltainfoxml2solv
/usr/local/include/solv/repo_write.h
/usr/local/lib64/libsolv.so
/usr/local/include/solv/tools_util.h
/usr/local/include/solv/dataiterator.h
/usr/local/lib64/libsolvext.so.0
/usr/lib64/python3.4/site-packages/__pycache__/solv.cpython-34.pyc
/usr/local/bin/updateinfoxml2solv
/usr/local/include/solv/dirpool.h
/usr/local/include/solv/poolvendor.h
/usr/local/include/solv/bitmap.h
/usr/local/include/solv/pool_fileconflicts.h
/usr/local/include/solv/strpool.h
/usr/local/include/solv/solverdebug.h
/usr/local/share/man/man1/rpms2solv.1
/usr/local/share/man/man1/dumpsolv.1
/usr/local/include/solv/selection.h
/usr/local/share/man/man3/libsolv-bindings.3
/usr/lib64/python3.4/site-packages/solv.py
/usr/local/share/man/man1/repomdxml2solv.1
/usr/local/lib64/libsolvext.so
/usr/local/include/solv/repo_deltainfoxml.h
/usr/local/include/solv/repo.h
/usr/local/bin/dumpsolv
/usr/local/include/solv/pooltypes.h
/usr/local/share/man/man3/libsolv-history.3
/usr/local/share/cmake/Modules/FindLibSolv.cmake
/usr/local/share/man/man1/deltainfoxml2solv.1
/usr/local/bin/mergesolv
/usr/local/bin/repo2solv.sh
/usr/local/include/solv/repo_repomdxml.h
/usr/local/lib64/pkgconfig/libsolv.pc
/usr/local/include/solv/solver.h
/usr/local/include/solv/pool.h
/usr/local/include/solv/repo_solv.h
/usr/local/bin/rpms2solv
/usr/local/include/solv/queue.h
/usr/local/share/man/man3/libsolv-pool.3
/usr/local/include/solv/chksum.h
/usr/local/bin/rpmdb2solv
/usr/local/share/man/man1/rpmmd2solv.1
/usr/local/include/solv/hash.h
/usr/local/include/solv/poolid.h
/usr/local/share/man/man3/libsolv-constantids.3

