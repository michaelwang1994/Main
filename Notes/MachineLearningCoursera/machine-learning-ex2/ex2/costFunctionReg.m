function [J, grad] = costFunctionReg(theta, X, y, lambda)
%COSTFUNCTIONREG Compute cost and gradient for logistic regression with regularization
%   J = COSTFUNCTIONREG(theta, X, y, lambda) computes the cost of using
%   theta as the parameter for regularized logistic regression and the
%   gradient of the cost w.r.t. to the parameters. 

% Initialize some useful values
m = length(y); % number of training examples
n = eye(length(theta));
n(1,1) = 0;
n1 = ones(length(theta),1);
n1(1) = 0;
% You need to return the following variables correctly 
J = 0;
grad = zeros(size(theta));

% ====================== YOUR CODE HERE ======================
% Instructions: Compute the cost of a particular choice of theta.
%               You should set J to the cost.
%               Compute the partial derivatives and set grad to the partial
%               derivatives of the cost w.r.t. each parameter in theta

predictions = sigmoid(X * theta);

J = (1/m)*(-y'* log(predictions) - (1-y)' * log(1-predictions)) + (lambda/(2*m)*n1'*(theta.^2));

grad = (1/m)*X'*(predictions - y)+(lambda/m)*n*theta;

% =============================================================

end
