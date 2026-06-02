Add-Type -AssemblyName System.Drawing
$srcPath = "C:\Users\Tony\.gemini\antigravity\scratch\tonyenglish-app\public\logo-square.png"
$img = [System.Drawing.Image]::FromFile($srcPath)

function Resize-Image($destPath, $size) {
    $bmp = New-Object System.Drawing.Bitmap $size, $size
    $g = [System.Drawing.Graphics]::FromImage($bmp)
    $g.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
    $g.DrawImage($img, 0, 0, $size, $size)
    $bmp.Save($destPath, [System.Drawing.Imaging.ImageFormat]::Png)
    $g.Dispose()
    $bmp.Dispose()
}

Resize-Image "C:\Users\Tony\.gemini\antigravity\scratch\tonyenglish-app\public\logo192.png" 192
Resize-Image "C:\Users\Tony\.gemini\antigravity\scratch\tonyenglish-app\public\logo512.png" 512

$img.Dispose()
