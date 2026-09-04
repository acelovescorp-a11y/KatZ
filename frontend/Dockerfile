FROM ubuntu:22.04 as base

RUN apt-get update && apt-get install -y \
    curl \
    git \
    unzip \
    libglu1-mesa \
    && rm -rf /var/lib/apt/lists/*

# Install Flutter
WORKDIR /app
RUN git clone https://github.com/flutter/flutter.git /flutter
ENV PATH="/flutter/bin:${PATH}"

RUN flutter config --no-analytics
RUN flutter precache

FROM base as builder

COPY . /app
WORKDIR /app/frontend

RUN flutter pub get
RUN flutter build apk --release --no-sound-null-safety

FROM base as final

COPY --from=builder /app/frontend/build/app/outputs/apk/release/app-release.apk .

CMD ["echo", "APK built successfully"]
