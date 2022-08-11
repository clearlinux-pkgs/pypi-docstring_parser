#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-docstring_parser
Version  : 0.14.1
Release  : 8
URL      : https://files.pythonhosted.org/packages/89/a9/b4f5b20cf96ed729dba274372e0e7cddf5aa1097bd5313d3cb074acb8854/docstring_parser-0.14.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/89/a9/b4f5b20cf96ed729dba274372e0e7cddf5aa1097bd5313d3cb074acb8854/docstring_parser-0.14.1.tar.gz
Summary  : Parse Python docstrings in reST, Google and Numpydoc format
Group    : Development/Tools
License  : MIT
Requires: pypi-docstring_parser-license = %{version}-%{release}
Requires: pypi-docstring_parser-python = %{version}-%{release}
Requires: pypi-docstring_parser-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(poetry_core)

%description
docstring_parser
================
[![Build](https://github.com/rr-/docstring_parser/actions/workflows/build.yml/badge.svg)](https://github.com/rr-/docstring_parser/actions/workflows/build.yml)

%package license
Summary: license components for the pypi-docstring_parser package.
Group: Default

%description license
license components for the pypi-docstring_parser package.


%package python
Summary: python components for the pypi-docstring_parser package.
Group: Default
Requires: pypi-docstring_parser-python3 = %{version}-%{release}

%description python
python components for the pypi-docstring_parser package.


%package python3
Summary: python3 components for the pypi-docstring_parser package.
Group: Default
Requires: python3-core
Provides: pypi(docstring_parser)

%description python3
python3 components for the pypi-docstring_parser package.


%prep
%setup -q -n docstring_parser-0.14.1
cd %{_builddir}/docstring_parser-0.14.1
pushd ..
cp -a docstring_parser-0.14.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656407005
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-docstring_parser
cp %{_builddir}/docstring_parser-0.14.1/LICENSE.md %{buildroot}/usr/share/package-licenses/pypi-docstring_parser/1290bb40923a9df1ab0612e35b07720062b32287
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-docstring_parser/1290bb40923a9df1ab0612e35b07720062b32287

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
