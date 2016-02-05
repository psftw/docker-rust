FROM debian:jessie

# rust beta 2016-02-04

# pub   4096R/FA1BE5FE 2013-09-26
#       Key fingerprint = 108F 6620 5EAE B0AA A8DD  5E1C 85AB 96E6 FA1B E5FE
# uid                  Rust Language (Tag and Release Signing Key) <rust-key@rust-lang.org>
RUN gpg --keyserver ha.pool.sks-keyservers.net --recv-keys 108F66205EAEB0AAA8DD5E1C85AB96E6FA1BE5FE

ENV RUST_SIGNATURE_SHA256 72387f0859b07d9c552b105d2a405ad7d41d5c56c1aa203302df64b29104c5fa

RUN set -x \
	&& apt-get update && apt-get install -y --no-install-recommends ca-certificates curl && rm -rf /var/lib/apt/lists/* \
	&& curl -fsSL "https://static.rust-lang.org/dist/2016-02-04/rust-beta-x86_64-unknown-linux-gnu.tar.gz" -o rust.tar.gz \
	&& curl -fsSL "https://static.rust-lang.org/dist/2016-02-04/rust-beta-x86_64-unknown-linux-gnu.tar.gz.asc" -o rust.tar.gz.asc \
	&& echo "$RUST_SIGNATURE_SHA256 rust.tar.gz.asc" | sha256sum -c - \
	&& gpg --verify rust.tar.gz.asc \
	&& mkdir rust \
	&& tar -xf rust.tar.gz -C rust --strip-components 1 \
	&& ( cd rust && ./install.sh ) \
	&& rm -r rust.tar.gz* rust \
 	&& apt-get purge -y --auto-remove curl
