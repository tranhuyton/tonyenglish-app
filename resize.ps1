Add-Type -AssemblyName System.Drawing
$img = [System.Drawing.Image]::FromFile("C:\Users\Tony\.gemini\antigravity\scratch\tonyenglish-app\public\logo-shield.png")
$size = [Math]::Max($img.Width, $img.Height)
$bmp = New-Object System.Drawing.Bitmap $size, $size
$g = [System.Drawing.Graphics]::FromImage($bmp)
$g.Clear([System.Drawing.Color]::Transparent)
$x = [int](($size - $img.Width) / 2)
$y = [int](($size - $img.Height) / 2)
$g.DrawImage($img, $x, $y, $img.Width, $img.Height)
$bmp.Save("C:\Users\Tony\.gemini\antigravity\scratch\tonyenglish-app\public\logo-square.png", [System.Drawing.Imaging.ImageFormat]::Png)
$g.Dispose()
$bmp.Dispose()
$img.Dispose()
