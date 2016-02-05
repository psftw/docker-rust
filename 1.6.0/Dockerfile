FROM debian:jessie

# rust 1.6.0 2016-01-21

# pub   4096R/FA1BE5FE 2013-09-26
#       Key fingerprint = 108F 6620 5EAE B0AA A8DD  5E1C 85AB 96E6 FA1B E5FE
# uid                  Rust Language (Tag and Release Signing Key) <rust-key@rust-lang.org>
RUN gpg --keyserver ha.pool.sks-keyservers.net --recv-keys 108F66205EAEB0AAA8DD5E1C85AB96E6FA1BE5FE

ENV RUST_SIGNATURE_SHA256 59f5e5d3033c2de440832a0b8af5b9cf54c1a9fef2b7d4fbe1778284305f5809

RUN set -x \
	&& apt-get update && apt-get install -y --no-install-recommends ca-certificates curl && rm -rf /var/lib/apt/lists/* \
	&& curl -fsSL "https://static.rust-lang.org/dist/2016-01-21/rust-1.6.0-x86_64-unknown-linux-gnu.tar.gz" -o rust.tar.gz \
	&& curl -fsSL "https://static.rust-lang.org/dist/2016-01-21/rust-1.6.0-x86_64-unknown-linux-gnu.tar.gz.asc" -o rust.tar.gz.asc \
	&& echo "$RUST_SIGNATURE_SHA256 rust.tar.gz.asc" | sha256sum -c - \
	&& gpg --verify rust.tar.gz.asc \
	&& mkdir rust \
	&& tar -xf rust.tar.gz -C rust --strip-components 1 \
	&& ( cd rust && ./install.sh ) \
	&& rm -r rust.tar.gz* rust \
 	&& apt-get purge -y --auto-remove curl
