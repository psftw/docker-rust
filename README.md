# Rust Docker images

Some incomplete work on a set of Rust-lang Docker images.

*   `update.py` regenerates Dockerfiles based on available releases.
*   `./build.sh` builds the corresponding `rust:*` Docker images.

## WIP

Do you want to maintain something like this as an Official Repository? Bonus
points for being involved in Rust-lang development.  There is still significant
work needed, such as:

*   Images should not run as root by default.
*   Testing -- do popular crates build?  Against which Rust versions?  What additional libraries and toolchains are needod to support the most common use cases?
*   Automate the update/test/commit/push process
*   Investigate minimal image variants and alterates (i.e. musl).
