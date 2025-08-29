# Set the base image with a default version
FROM debian@sha256:731dd1380d6a8d170a695dbeb17fe0eade0e1c29f654cf0a3a07f372191c3f4b AS builder

# Set noninteractive env for apt-get to avoid prompts
ENV DEBIAN_FRONTEND=noninteractive

# Define arguments for versions
ARG GCC_VERSION=11.3.0-12
ARG LLVM_VERSION=16.0.6-15

# Update package list and install dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        wget=1.21.3-1+deb12u1 \
        git=1:2.39.5-0+deb12u2 \
        git-lfs=3.3.0-1+deb12u1 \
        graphviz=2.42.2-7+deb12u1 \
        default-jre=2:1.17-74 \
        libtinfo5=6.4-4 \
        g++-${GCC_VERSION} \
        gdb=13.1-3 \
        googletest=1.12.1-0.2 \
        gcovr=5.2-1 \
        cmake=3.25.1-1 \
        clang-${LLVM_VERSION} \
        clang-tidy-${LLVM_VERSION} \
        clang-format-${LLVM_VERSION} \
        doxygen=1.9.4-4 \
        curl \
        make \
        python3 \
        python3-pip=23.0.1+dfsg-1 \
        python3-venv \
        pipx \
        locales \
        ssh-client \
    && apt-get clean && \
    rm -rf bazel-bin bazel-inc_json bazel-out bazel-testlogs && \
    rm -rf /var/lib/apt/lists/*

# Generate and set the locale
RUN echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen && \
    locale-gen en_US.UTF-8 && \
    update-locale LANG=en_US.UTF-8

# Environment variables for locale
ENV LANG=en_US.UTF-8
ENV LC_ALL=en_US.UTF-8

COPY ./S-CORE/requirements.txt ./S-CORE/requirements.txt
RUN python3 -m venv venv && \
    . venv/bin/activate && \
    pip install --require-hashes -r ./S-CORE/requirements.txt

# Specify default versions via update alternatives
RUN update-alternatives --install /usr/bin/clang-tidy clang-tidy /usr/bin/clang-tidy-16 100 && \
    update-alternatives --set clang-tidy /usr/bin/clang-tidy-16 && \
    update-alternatives --install /usr/bin/clang-format clang-format /usr/bin/clang-format-16 100 && \
    update-alternatives --set clang-format /usr/bin/clang-format-16 && \
    update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-11 100 && \
    update-alternatives --set g++ /usr/bin/g++-11

# Install bazelisk tool
RUN wget https://github.com/bazelbuild/bazelisk/releases/download/v1.26.0/bazelisk-linux-amd64 && \
    chmod +x bazelisk-linux-amd64 && \
    mv bazelisk-linux-amd64 /usr/local/bin/bazel

# Install buildifier
RUN wget https://github.com/bazelbuild/buildtools/releases/download/v8.2.0/buildifier-linux-amd64 && \
    chmod +x buildifier-linux-amd64 && \
    mv buildifier-linux-amd64 /usr/bin/buildifier

# Create non-root user
ARG USERNAME=developer
ARG USER_UID=1000
ARG USER_GID=$USER_UID

RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
    # Add sudo support
    && apt-get update \
    && apt-get install -y sudo \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME

# Default user
USER $USERNAME

# Install trudag using pipx
RUN pipx install git+https://gitlab.com/CodethinkLabs/trustable/trustable@cc6b72753e1202951d382f60ff08320f5a957c7b && \
    pipx ensurepath
