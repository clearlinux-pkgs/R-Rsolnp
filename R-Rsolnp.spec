#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-Rsolnp
Version  : 1.16
Release  : 11
URL      : https://cran.r-project.org/src/contrib/Rsolnp_1.16.tar.gz
Source0  : https://cran.r-project.org/src/contrib/Rsolnp_1.16.tar.gz
Summary  : General Non-Linear Optimization
Group    : Development/Tools
License  : GPL-2.0
BuildRequires : R-truncnorm
BuildRequires : buildreq-R

%description
No detailed description available

%prep
%setup -q -c -n Rsolnp

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552954207

%install
export SOURCE_DATE_EPOCH=1552954207
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library Rsolnp
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library Rsolnp
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library Rsolnp
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc  Rsolnp || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/Rsolnp/CITATION
/usr/lib64/R/library/Rsolnp/COPYRIGHTS
/usr/lib64/R/library/Rsolnp/DESCRIPTION
/usr/lib64/R/library/Rsolnp/INDEX
/usr/lib64/R/library/Rsolnp/Meta/Rd.rds
/usr/lib64/R/library/Rsolnp/Meta/features.rds
/usr/lib64/R/library/Rsolnp/Meta/hsearch.rds
/usr/lib64/R/library/Rsolnp/Meta/links.rds
/usr/lib64/R/library/Rsolnp/Meta/nsInfo.rds
/usr/lib64/R/library/Rsolnp/Meta/package.rds
/usr/lib64/R/library/Rsolnp/NAMESPACE
/usr/lib64/R/library/Rsolnp/R/Rsolnp
/usr/lib64/R/library/Rsolnp/R/Rsolnp.rdb
/usr/lib64/R/library/Rsolnp/R/Rsolnp.rdx
/usr/lib64/R/library/Rsolnp/doc/manual.pdf
/usr/lib64/R/library/Rsolnp/help/AnIndex
/usr/lib64/R/library/Rsolnp/help/Rsolnp.rdb
/usr/lib64/R/library/Rsolnp/help/Rsolnp.rdx
/usr/lib64/R/library/Rsolnp/help/aliases.rds
/usr/lib64/R/library/Rsolnp/help/paths.rds
/usr/lib64/R/library/Rsolnp/html/00Index.html
/usr/lib64/R/library/Rsolnp/html/R.css
