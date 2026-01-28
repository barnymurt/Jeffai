#!/bin/bash
# Bundle React artifact into single HTML file

set -e

echo "🔗 Bundling React artifact to single HTML file..."

# Check if index.html exists
if [ ! -f "index.html" ]; then
    echo "❌ Error: index.html not found in current directory"
    echo "Make sure you're in the project root and have an index.html file"
    exit 1
fi

# Check if node_modules exists
if [ ! -d "node_modules" ]; then
    echo "📦 Installing dependencies..."
    npm install
fi

# Install bundling dependencies if not present
echo "📦 Installing bundling dependencies..."
npm install --save-dev parcel@^2.9.0 @parcel/config-default parcel-resolver-tspaths html-inline@^1.2.0

# Build with Parcel (no source maps for cleaner output)
echo "🏗️  Building project with Parcel..."
npx parcel build index.html --dist-dir dist --no-source-maps --public-url ./

# Check if build was successful
if [ ! -f "dist/index.html" ]; then
    echo "❌ Build failed - dist/index.html not found"
    exit 1
fi

# Inline all assets into single HTML file
echo "📝 Inlining assets into single HTML file..."
npx html-inline dist/index.html -o bundle.html

# Verify bundle was created
if [ ! -f "bundle.html" ]; then
    echo "❌ Bundle failed - bundle.html not created"
    exit 1
fi

# Get file size
BUNDLE_SIZE=$(du -h bundle.html | cut -f1)

echo "✅ Bundle created successfully!"
echo "📄 File: bundle.html ($BUNDLE_SIZE)"
echo ""
echo "🚀 Your artifact is ready! Share bundle.html in your Claude conversation."

# Optional: Clean up dist directory
rm -rf dist

echo "🧹 Cleaned up build artifacts"