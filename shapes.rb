# Test file for cloe-test-repo — feel free to read, edit, or delete this.
class Shape
  def area
    raise NotImplementedError, "Subclass must implement area"
  end

  def perimeter
    raise NotImplementedError, "Subclass must implement perimeter"
  end

  def to_s
    "#{self.class.name}: area=#{area.round(2)}, perimeter=#{perimeter.round(2)}"
  end
end

class Circle < Shape
  attr_reader :radius

  def initialize(radius)
    @radius = radius
  end

  def area
    Math::PI * radius ** 2
  end

  def perimeter
    2 * Math::PI * radius
  end
end

class Rectangle < Shape
  attr_reader :width, :height

  def initialize(width, height)
    @width = width
    @height = height
  end

  def area
    width * height
  end

  def perimeter
    2 * (width + height)
  end
end

class Triangle < Shape
  attr_reader :a, :b, :c

  def initialize(a, b, c)
    raise ArgumentError, "Invalid triangle" unless valid?(a, b, c)
    @a, @b, @c = a, b, c
  end

  def area
    s = perimeter / 2.0
    Math.sqrt(s * (s - a) * (s - b) * (s - c))
  end

  def perimeter
    a + b + c
  end

  private

  def valid?(a, b, c)
    a + b > c && a + c > b && b + c > a
  end
end

shapes = [
  Circle.new(5),
  Rectangle.new(4, 6),
  Triangle.new(3, 4, 5),
]

shapes.each { |s| puts s }
# End of test file.
